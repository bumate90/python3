#!/usr/bin/python3.7.9

#############################################################################
#                        HOW TO INSTALL ptyhon 3.7.9                        #
#############################################################################
# https://tecadmin.net/install-python-3-7-on-ubuntu-linuxmint/
# cd /usr/src
# sudo wget https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz
# sudo tar xzf Python-3.7.9.tgz
# cd Python-3.7.9
# sudo ./configure --enable-optimizations
# sudo make altinstall
#############################################################################


class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod(str):
        print(f"static method called - {str}")


# F-String example
name = "Mate Budai"
print(f"They call him {name}!")

def foo():
    print("foo()")

def bar():
    print("bar()")

breakpoint()
obj = MyClass()
# All 3 works
obj.method()
obj.classmethod()
obj.staticmethod('test')
# The first one fails
# MyClass.method()
MyClass.classmethod()
MyClass.staticmethod('test')

foo()
# pdb.set_trace is the old style
#import pdb; pdb.set_trace()
breakpoint()
bar()