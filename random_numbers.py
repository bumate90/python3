#!/usr/bin/python3.7.9

#############################################################################
#                                RANDOM NUMBERS                             #
#############################################################################


from random import randrange, uniform, randint
# randrange gives you an integral value
irand = randrange(0, 10)
print(irand)

# uniform gives you a floating-point value
frand = uniform(100, 101)
print(frand)

#This generates 10 pseudorandom integers in range 0 to 9 inclusive.
x = [randint(0, 9) for p in range(0, 10)]
print(x)