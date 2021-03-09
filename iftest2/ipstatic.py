#!/usr/bin/env python3
# This line now pormpts the user for input
ipchk = input("Apply an IP Address") 

# if user set IP of Gateway
if ipchk == "192.168.70.1":
    print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
# a provided string will test true
elif ipchk:
   print("Looks like the IP address was set: " + ipchk)

else:   # if data is NOT provided
    print("You did NOT provide input.")

