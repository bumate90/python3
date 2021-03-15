#!/usr/bin/python3.7.9

#############################################################################
#                                Datatypes                                  #
#############################################################################

breakpoint()
# String
# Here we can see the three types of indexing!
# ---------------------------
str = "Python 3 crash course"
#print(str[7])
#print(str[9:14])
#print(str[9:])
#print(str[:6])
print(type(str))


# Int
# ---------------------------
val = 5
print(type(val))


# Float
# ---------------------------
val2 = 3.14
print(type(val2))


# List
# ---------------------------
mylist = [4,8,15,16,23,42]
#mylist.append(911)
#print(mylist[0])
print(type(mylist))


# Bool
# ---------------------------
flag = True
print(type(flag))


# Dictionary
# ---------------------------
mydict = dict(username="budaimat",
              age=31,
              realname="Mate Budai",
              location="EU")
#print(mydict["age"])
#mydict["newkey"]="newvalue"
print(type(mydict))


# Tuple
# FYI: Same as list, but it cannot change. Tuples are immutable.
# ---------------------------
mytuple = ("Meow", "Woof")
#print(mytuple[1])
print(type(mytuple))


# Set
# FYI: Holds only unique items
# Will print {'Pizza', 'Burger', 'Tacos', 'Icecream'}
# ---------------------------
myset = {"Icecream","Pizza","Tacos","Burger","Pizza", "Tacos", "Pizza"}
#myset.add("Pizza")
#print(myset)
print(type(myset))