#!/usr/bin/python3.7.9

#############################################################################
#                                  FIGLET                                   #
#############################################################################

# A python module, which converts ASCII text into ASCII art fonts

# Must be installed
# pip3 install pyfiglet
# NEEDS pip3 (python3 package manager)
# sudo apt install python3-pip

# import pyfiglet module
import pyfiglet
  
result = pyfiglet.figlet_format("Mate Budai")
print(result)
