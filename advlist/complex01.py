#!/usr/bin/env python3

# create a list called list1
list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]
# display list1
print(list1)
# display list1[1] which should only display arista_eos
print(list1[1])
# Create a new list containning a single item
list2 = ["juniper"]
# Extend list1 bu list2 (combine both lists together into a single list)
list1.extend(list2)
# Display list1, which now contains juniper
print(list1)
# Create list3
list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]
list1.append(list3)
print(list1)
# Display a list of IP addresses
print(list1[4])
# Disdplay the first item in the list (0th item) - first IP Address
print(list1[4][0])
