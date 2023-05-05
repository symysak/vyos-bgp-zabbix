import json
import subprocess

cmd = ["sudo", "vtysh", "-c", "show bgp neighbors"]
res = subprocess.check_output(cmd, encoding="utf-8")

filtered_res = subprocess.check_output(["grep", "BGP neighbor is"], input=res, encoding="utf-8")

lines = filtered_res.strip().split("\n")
neigh_ips = []

for line in lines:
    fields = line.split()
    neigh_ips.append(fields[3].strip(","))

result = {"data": []}
for ip in neigh_ips:
    result["data"].append({"{#NEIGHBOR_IP_ADDR}": ip})

print(json.dumps(result))