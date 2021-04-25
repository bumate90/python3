#!/usr/bin/python3.7.9

#############################################################################
#                                  LOOPS                                    #
#############################################################################


# FOR
#----------------------------------------------------------------------------

# looping through elements
# iterables - set, tuple, list, dict, string
my_list = ["Banana", "Mango", "Pineapple", "Blueberries"]
for element in my_list:
    print(f"The element is {element}")

# looping through keys
my_dict = dict(name='Mate Budai', age=31, location='Budapest')
for item in my_dict:
    print(f"key: {item}, value: {my_dict[item]}")

name = " Mate Budai "
# print all letters lowercase
for letter in name:
    print(letter.lower())

# remove the whitespace from both ends
# printing just the fist name
name = name.strip()
for l in name:
    if l == ' ':
        print()
        break
    else:
        #printing without newline at the end
        print(l, end="")


# WHILE
#----------------------------------------------------------------------------

# Print all even numbers below 100
num = 2
while num < 100:
    print(f"{num} ", end="")
    num+=2
print()

# List comprehension
#----------------------------------------------------------------------------
numbers = [0,1,2,3,4,5,6,7,8,9]
numbers_even_scaled_by_ten = [num*10 for num in numbers if num % 2 == 0]
print(numbers_even_scaled_by_ten)
