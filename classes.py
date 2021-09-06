#!/usr/bin/python3.7.9

#############################################################################
#                             CLASSES & DECORATORS                          #
#############################################################################

# DECORATORS:
# @property
# this decorator allows us to use this method as a class property

# @classmethod	                                                                    @staticmethod
# Declares a class method.	                                                        Declares a static method.
# It can access class attributes, but not the instance attributes.	                It cannot access either class attributes or instance attributes.
# It can be called using the ClassName.MethodName() or object.MethodName().	        It can be called using the ClassName.MethodName() or object.MethodName().
# It can be used to declare a factory method that returns objects of the class.	    It cannot return an object of the class.

# Writing our own decorator called overrides to improve code readability
def overrides(interface_class):
    """
    Function override annotation.
    """
    def overrider(method):
        assert(method.__name__ in dir(interface_class))
        return method

    return overrider

class Person():

    number_of_people = 0    # class attribute shared among all instances of this class

    # The __init__ method for initialization is invoked without any call, when an instance of a class is created,
    # like constructors in certain other programming languages such as C++
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name    # instance attribute, unique
        self.last_name = last_name
        self.age = age
        Person.number_of_people += 1

    def print(self):
        print(f"Person::print() - This is {self.first_name}, age {self.age}.")

    @property
    def full_name(self):
        return self.first_name + " " +self.last_name

    @classmethod
    def get_num_of_people(cls):
        return cls.number_of_people

    @staticmethod
    def module_name():
        return 'Classes and decorators'

    # Dunder or magic methods in Python are the methods having two prefix and suffix underscores in the method name.
    # Dunder here means “Double Under (Underscores)”. These are commonly used for operator overloading.
    # Few examples for magic methods are: __init__, __add__, __len__, __repr__ etc.
    # These methods are the reason we can add two strings with ‘+’ operator without any explicit typecasting.
    def __len__(self):
        return len(self.first_name) + len(self.last_name) + 1


# inheriting from Person
class Employee(Person):

    def __init__(self, first_name, last_name, age, role):
        # calling base class constructor
        super(Employee, self).__init__(first_name, last_name, age)
        self.role = role

    @overrides(Person)
    def print(self):
        # calling base class print
        super().print()
        print(f"Employee::print() - His role is {self.role}!")


# When your script is run by passing it as a command to the Python interpreter,
# python myscript.py
# all of the code that is at indentation level 0 gets executed.
# Functions and classes that are defined are, well, defined, but none of their code gets run.
# Unlike other languages, there's no main() function that gets run automatically - the main() function is implicitly all the code at the top level.

# __name__ is a built-in variable which evaluates to the name of the current module.
# However, if a module is being run directly (as in myscript.py above), then __name__ instead is set to the string "__main__".
# Thus, you can test whether your script is being run directly or being imported by something else by testing

# if __name__ == "__main__":
#     ...
# If your script is being imported into another module, its various function and class definitions will be imported
# and its top-level code will be executed, but the code in the then-body of the if clause above won't get run as the condition is not met.
# TLDR: It's boilerplate code that protects users from accidentally invoking the script when they didn't intend to.
if __name__ == '__main__':
    p1 = Person("Mate", "Budai", 31)
    p1.print()

    # we can do this since we have the __len__ dunder method defined
    print(f"Length of p1: {len(p1)}")

    e1 = Employee("Mate", "Budai", 31, "developer")
    e1.print()

    # property decorator
    print(e1.full_name)
    # staticmethod decorator - class name has to be specified but NO object is needed
    print(Person.module_name())
    # classmethod decorator - same as staticmethod, but it can also access class attributes
    print(Person.get_num_of_people())
