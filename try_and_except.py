#!/usr/bin/python3.7.9

#############################################################################
#                                TRY AND EXCEPT                             #
#############################################################################
#
# More on this topic under:
# https://docs.python.org/3/tutorial/errors.html
#
# Most common errors are:
# SyntaxError, ZeroDivisionError, NameError, TypeError, ValueError, OSError


# EXAMPLE1 - simple exception handling
print("EXAMPLE1:")
try:
    1/0 #--->ZeroDivisionError: division by zero
except Exception as e:
    print(e)
    print(type(e))

# because we caught the exception exectuion continues
print("Exectuion continues...")
print("-----------------------------------------------")


# EXAMPLE2 - safe division
print("EXAMPLE2:")
def safe_divison():
    result = float('nan')
    while(1):
        arg1 = input("Enter the 1st number: ")
        arg2 = input("Enter the 2nd number: ")
        try:
            arg1 = int(arg1)
            arg2 = int(arg2)
        except ValueError:
            # Handle the exception
            print('Please enter an integer')
            continue

        try:
            result = arg1 / arg2
        except ZeroDivisionError:
            print("Division by zero is not allowed!")
            continue
        break
    print(f"result: {result}")
    return result

#safe_divison()
print("-----------------------------------------------")


# EXAMPLE3 - finally
# The finally clause is always executed
# When a return, break or continue statement is executed in the try suite of a try…finally statement,
# the finally clause is also executed ‘on the way out.’
# THIS MEANS:
# !!!You can use finally to make sure files or resources are closed or released regardless of whether an exception occurs, even if you don't catch the exception!!!
print("EXAMPLE3:")

def f(arg1, arg2):
    result = float('nan')
    print("Opening result.txt")
    file = open("result.txt", "w")
    try:
        result = arg1 + arg2
        file.write(str(result))
        print(f"{result} written")
    except TypeError as e:
        pass
    finally:
        print("Closing result.txt...")
        file.close()

f(2, 2) # this will write 4
f(2, '2') # this will cause a TypeError -> nevertheless our file is closed!
print("-----------------------------------------------")


# EXAMPLE4 - raise statement and inheriting from Exception
# The raise statement allows the programmer to force a specified exception to occur.
print("EXAMPLE4:")

class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.salary} -> {self.message}'

salary = int(input("Enter salary amount: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)
