#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Conditionals - strings test true"""

#ipchk = "192.168.0.1"

# a string tests as True
#if ipchk:
#   print("Looks like the IP address was set: " + ipchk)

ipchk = input("Apply an IP address: ") # this line now prompts the user for input

# a provided string will test true
#if ipchk:
#   print("Looks like the IP address was set: " + ipchk) # indented under if

# a provided string will test true
#if ipchk:
#   print("Looks like the IP address was set: " + ipchk) # indented under if
#else:    # if data is NOT provided
#   print("You did not provide input.") # indented under else

# if user set IP of gateway
if ipchk == "192.168.70.1":
   print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
elif ipchk: # if any data is provided, this will test true
   print("Looks like the IP address was set: " + ipchk) # indented under if
else: # if data is NOT provided
   print("You did not provide input.") # indented under else
