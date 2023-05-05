import sys
import subprocess

args = sys.argv

cmd = ["sudo", "vtysh", "-c", "show bgp neighbor " + args[1]]
res = subprocess.check_output(cmd, encoding="utf-8")
filtered_res = subprocess.check_output(["grep", "BGP state = "], input=res, encoding="utf-8")

fields = filtered_res.split()
result = -1
if fields[3] == "Idle,":
    result = 1
elif fields[3] == "Connect,":
    result = 2
elif fields[3] == "Active,":
    result = 3
elif fields[3] == "Open Sent,":
    result = 4
elif fields[3] == "Open Confirm,":
    result = 5
elif fields[3] == "Established,":
    result = 6
else:
    result = -1
print(result)