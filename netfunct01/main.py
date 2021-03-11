#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""
# Importing Colorama
#from colorama import init
#from termcolor import colored
#init()
# function to push commands
def commandpush(devicecmd): # devicecmd==list
    for coffeetime in devicecmd.keys():
        print('Handshaking. .. ... connecting with ' + coffeetime )
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[coffeetime]:
            print('Attempting to send command --> ' + mycmds )
            # we'll learn to write code that sends cmds to device here
            
# Second Function to Reboot 
def devicereboot(devicecmd):  # devicemds==list
    for reboot in devicecmd:
    # this first for loop will go across all the elements in the list:
    # 8.8.8.8 will be the first value of reboot
    # 7.7.7.7 will be the second value of reboot, and so on.
        # this line looks good!
        print('Handshaking......Connecting with ' + reboot )
        # the challenge says that next it should print REBOOTING NOW
        print("REBOOTING NOW!")

        
        
        # we don't need these lines, this is for slicing through the work2do dictionary
        #for mycmds in devicecmd[reboot]:
           # print('Attempting to send reboot command ---> ' + mycmds )

# start our main script
def main():
    work2do = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]} 
    # data that replaces data stored in file

    print("Welcome to the network device command pusher") # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(work2do) # call function to push commands to devices

    ## Run for reboot
    #work2do2 = {"10.2.0.1":["reboot"]}
    ##### The challenge calls for a list of IPs, so let's make a list:
    iplist= ["8.8.8.8","7.7.7.7","6.6.6.6"]


    # data that replaces data stored in file
    print("Welcome to the network device command pusher") # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    devicereboot(iplist) # call function to push commands to devices
    ##### now we're pushing that list to the devicereboot function

# call our main function
main()

