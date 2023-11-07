#!/usr/bin/env python3

"""Tony | TLG Learning
   Copying files using shutil from standard library"""


# import modules shutil and os
import shutil
import os

def main():

    # change to /home/students/mycode directory
    os.chdir("/home/student/mycode/")

    # make a copy of the sdn_network.txt file
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    # make a copy of the entire 5g_research directory
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__:
    main()



        
