# Kubernetes Resource Monitoring
### Feature
- Generate JSON data for every container complete with CPU, memory, and timestamp where the data taken
- Generate text data in fashionable way for average CPU and memory resource usage for every pod

### How to Use
```
virtualenv .
source bin/active
pip install -r requirements.txt
python app.py <NAMESPACE> <CONTAINER_NAME>
// Press [[ Ctrl + C ]] to stop the program
```

### Output
#### Console stdout
```
+---------------------------------------------+--------------------------------+----------------------------+
|                   POD_NAME                  | AVERAGE CPU USAGE in millicore | AVERAGE MEMORY USAGE in MB |
+---------------------------------------------+--------------------------------+----------------------------+
| your-kubernetes-service-f6dd9677b-r78jx     |             88.370             |           23.062           |
| your-kubernetes-service-f6dd9677b-7hmdz     |             88.700             |           19.648           |
| your-kubernetes-service-f6dd9677b-4snfp     |            103.161             |           26.562           |
| your-kubernetes-service-f6dd9677b-p2tqt     |             89.610             |           19.773           |
+---------------------------------------------+--------------------------------+----------------------------+
```
#### API JSON format
```
{"pods":{"your-kubernetes-service-f6dd9677b-4snfp":[{"cpu":"103160945n","memory":"27200Ki","timestamp":"24-03-2020 18:17:45"},{"cpu":"103160945n","memory":"27200Ki","timestamp":"24-03-2020 18:17:45"},{"cpu":"103160945n","memory":"27200Ki","timestamp":"24-03-2020 18:17:45"},{"cpu":"103160945n","memory":"27200Ki","timestamp":"24-03-2020 18:17:45"},{"cpu":"103160945n","memory":"27200Ki","timestamp":"24-03-2020 18:17:46"},{"cpu":"103160945n","memory":"27200Ki","timestamp":"24-03-2020 18:17:46"}],"your-kubernetes-service-f6dd9677b-7hmdz":[{"cpu":"88700234n","memory":"20120Ki","timestamp":"24-03-2020 18:17:45"},{"cpu":"88700234n","memory":"20120Ki","timestamp":"24-03-2020 18:17:45"},{"cpu":"88700234n","memory":"20120Ki","timestamp":"24-03-2020 18:17:45"},{"cpu":"88700234n","memory":"20120Ki","timestamp":"24-03-2020 18:17:45"},{"cpu":"88700234n","memory":"20120Ki","timestamp":"24-03-2020 18:17:46"},{"cpu":"88700234n","memory":"20120Ki","timestamp":"24-03-2020 18:17:46"}],"your-kubernetes-service-f6dd9677b-p2tqt":[{"cpu":"89609713n","memory":"20248Ki","timestamp":"24-03-2020 18:17:45"},{"cpu":"89609713n","memory":"20248Ki","timestamp":"24-03-2020 18:17:45"},{"cpu":"89609713n","memory":"20248Ki","timestamp":"24-03-2020 18:17:45"},{"cpu":"89609713n","memory":"20248Ki","timestamp":"24-03-2020 18:17:45"},{"cpu":"89609713n","memory":"20248Ki","timestamp":"24-03-2020 18:17:46"},{"cpu":"89609713n","memory":"20248Ki","timestamp":"24-03-2020 18:17:46"}],"your-kubernetes-service-f6dd9677b-r78jx":[{"cpu":"88369653n","memory":"23616Ki","timestamp":"24-03-2020 18:17:45"},{"cpu":"88369653n","memory":"23616Ki","timestamp":"24-03-2020 18:17:45"},{"cpu":"88369653n","memory":"23616Ki","timestamp":"24-03-2020 18:17:45"},{"cpu":"88369653n","memory":"23616Ki","timestamp":"24-03-2020 18:17:45"},{"cpu":"88369653n","memory":"23616Ki","timestamp":"24-03-2020 18:17:46"},{"cpu":"88369653n","memory":"23616Ki","timestamp":"24-03-2020 18:17:46"}]}}

```