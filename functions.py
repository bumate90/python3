#!/usr/bin/python3.7.9

#############################################################################
#                                 FUNCTIONS                                 #
#############################################################################

def name():
    return "Bob"

def greeting(name, greeting="Hello"):
    print(f"{name}, {greeting} to you good sir!")


my_name = name()
print(my_name)

greeting(name())

   