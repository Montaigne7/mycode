#!/usr/bin/env python3

import time

def main():
    #hostname = "MTG"

    #if hostname == "MTG":
    #    print("The hostname was found to be MTG")

    #hostname = input("What value should we set for hostname?")
    #if hostname == "MTG":
    #    print("The hostname was found to be MTG")

    hostname = input("What value should we set for hostname?")
    ## Notice how the next line has changed
    ## here we use the str.lower() method to return a lowercase string
    if hostname.lower() == "mtg":
        print("The hostname was found to be mtg")  
        time.sleep(1)
        print("Hostname matches expected config")

    time.sleep(1)
    print("Exiting Script")

main()