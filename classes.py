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

p1 = Person("Mate", "Budai", 31)
p1.print()

e1 = Employee("Mate", "Budai", 31, "developer")
e1.print()

# property decorator
print(e1.full_name)
# staticmethod decorator - class name has to be specified but NO object is needed
print(Person.module_name())
# classmethod decorator - same as staticmethod, but it can also access class attributes
print(Person.get_num_of_people())
