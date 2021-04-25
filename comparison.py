#!/usr/bin/python3.7.9

#############################################################################
#                            COMPARISON OPERATORS                           #
#############################################################################

# integer
tmp_int = 5
if tmp_int < 0:
    print("The value is negative!")
elif tmp_int == 0:
    print("The value equals zero!")
else:
    print(f"The value is positive({tmp_int})")

# none-type
value = None
if value is None:
    print("Value is None!")

# string
tmp_str = "test"
if tmp_str == "test":
    print("String comparison success!")

# list
tmp_list = [1,2,3,4,5]
if tmp_list == [1,2,3,4,5]:
    print("List comparison1 success!")
if tmp_list[4] == 5:
    print("List comparison2 success!")
if len(tmp_list) == 5:
    print("List comparison3 success!")

# dict
tmp_dict = dict(name="Mate Budai", age=31, location='Budapest')
tmp_dict2 = {'name':"Mate Budai", 'age':31, 'location':'Budapest'}
if tmp_dict['name'] =="Mate Budai":
    print("Dict comparison1 success!")
if len(tmp_dict) == 3:
    print("Dict comparison2 success!")
if list(tmp_dict.keys())[0] == 'name':
    print("Dict comparison3 success!")
if list(tmp_dict2.keys())[2] == 'location':
    print("Dict comparison4 success!")
if tmp_dict.get('age') == 31:
    print("Dict comparison5 success!")
