#!/usr/bin/env python3

#!/usr/bin/env python3
import subprocess  ## <-------- changed
#subprocess.call(["ip", "link", "show", "up"])
#print("This program will check your interfaces.")
#interface = input("Enter an interface, like, ens3: ")
#subprocess.call(["ip", "addr", "show", "dev", interface])  ## <--- changed
#subprocess.call(["ip", "route", "show", "dev", interface]) ## <--- changed

ip_a = ["ip", "a"]

subprocess.call(ip_a)

iproute = subprocess.call(["ip", "route"])

print(iproute)

cd = subprocess.call(["cd"])