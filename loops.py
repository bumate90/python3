#!/usr/bin/python3.7.9

#############################################################################
#                                  LOOPS                                    #
#############################################################################


# FOR
#----------------------------------------------------------------------------

# looping through elements
my_list = ["Banana", "Mango", "Pineapple", "Blueberries"]
for element in my_list:
    print(f"The element is {element}")

# looping through keys
my_dict = dict(name='Mate Budai', age=31, location='Budapest')
for item in my_dict:
    print(f"key: {item}, value: {my_dict[item]}")
