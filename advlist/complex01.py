#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - simple list"""

def main():
    # create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # display list1
    print(list1)

    # display arista_eos from list1
    print(list1[1])

    # new list containing singl item
    list2 = ["juniper"]

    # extend list1 with list2
    list1.extend(list2)
    
    #display new extended list1
    print(list1)
    
    # create list3
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

    # use the append operation to append list1 by list3
    list1.append(list3)

    # display new complex list
    print(list1)

    #display list of IP Addresses
    print(list1[4])

    #display first IP Address of list in the complex list
    print(list1[4][0])

main()
