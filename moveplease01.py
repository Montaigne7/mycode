#!/usr/bin/env python3

"""Tony |TLG Learning
    Move around files"""

import shutil
import os

def main():
    
    # the main function starts at runtime

    os.chdir("/home/student/mycode/") # change to working directory
    shutil.move("raynor.obj", "ceph_storage/") # move file raynor.obj into ceph_storage dir


    xname = input("What is the new name for kerrigan.obj? ") #get user input on new name for kerrigan.obj file  
    shutil.move("ceph_storage/kerrigan.obj", "ceph_storage/" + xname) # move 
    
main()

