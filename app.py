import os
import re
import sys
import kubernetes.client as client

from json import dumps
from datetime import datetime
from kubernetes import config
from kubernetes.stream import stream
from kubernetes.client import Configuration
from kubernetes.client.rest import ApiException
from subprocess import check_output
from prettytable import PrettyTable
from pprint import pprint

value = {}  # JSON root key 
current_time = datetime.today().strftime("%H:%M:%S")

table = PrettyTable()
table.field_names = ["KUBERNETES POD NAME", 
  "AVERAGE CPU USAGE in millicore", 
  "AVERAGE MEMORY USAGE in MB"]

try:
  namespace = sys.argv[1]
  container_name = sys.argv[2]
  kubeconfig = os.getenv("KUBECONFIG")
  config.load_kube_config(kubeconfig)
  c = client.Configuration()
  resource = client.CustomObjectsApi()
  api = client.CoreV1Api(client.ApiClient(c))
except IndexError:
  print("\033[91m[ERROR] Please set the positional arguments\033[0m")
  print("\033[91m1st positional argument: kubernetes namespace\033[0m")
  print("\033[91m2nd positional argument: pod container name\033[0m")
  print("\033[91mExample: python app.py <NAMESPACE> <CONTAINER_NAME>\033[0m")
  print("\033[91mExample: python app.py versusevil ds-game-accelbytetesting\033[0m")
  sys.exit(1)
except NameError:
  print("\033[91m[ERROR] Please set KUBECONFIG environment variable first\033[0m")
except config.config_exception.ConfigException:
  print("\033[91m[ERROR] Please check your KUBECONFIG value path is exist and readable\033[0m")
  print("\033[91m[ERROR] Your KUBECONFIG value is :: {}\033[0m".format(os.getenv("KUBECONFIG")))
except ApiException as error:
  print("\033[91m[ERROR] Please check the firewall or security group in your kubernetes cluster\033[0m")
  print(err)


def main():
  try:
    while True:
      for pod in resource.list_namespaced_custom_object("metrics.k8s.io", 
        "v1beta1", namespace, "pods")["items"]:
        containers = pod["containers"]
        pod_name = pod["metadata"]["name"]
        for index, container in enumerate(containers):
          if container["name"].startswith(container_name):
            used_resource = {}
            used_resource["cpu"] = pod["containers"][index]["usage"]["cpu"]
            used_resource["memory"] = pod["containers"][index]["usage"]["memory"]
            used_resource["timestamp"] = datetime.today().strftime("%d-%m-%Y %H:%M:%S")
            try: value[pod_name].append(used_resource)
            except KeyError: 
              value[pod_name] = [] # empty init val
              value[pod_name].append(used_resource)
  except NameError as error: print(error)
  except KeyboardInterrupt as error:
    print("\n")  # adding blank sep.
    no_alphabet = re.compile("[a-zA-Z]")
    for res_usage in value.items():
      total_cpu = 0
      total_memory = 0
      number_of_data = len(res_usage[1])
      for pod_res_usage in res_usage[1]:
        total_cpu = total_cpu + int(no_alphabet.sub("", pod_res_usage["cpu"]))
        total_memory = total_memory + int(no_alphabet.sub("", pod_res_usage["memory"]))
      table.add_row([res_usage[0], 
        "{0:.3f}".format(total_cpu/number_of_data/1000/1000), 
        "{0:.3f}".format(total_memory/number_of_data/1024)
      ])

    print(table)
    with open("resource_consumption.json", "w") as resource_usage:
      response = {"pods": value}
      resource_usage.write(dumps(response, indent=4, sort_keys=True))

main()
