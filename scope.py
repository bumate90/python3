#!/usr/bin/python3.7.9

#############################################################################
#                                   SCOPE                                   #
#############################################################################

# How python handles scope in really confusing, variable go in and out of function scopes


#----------------------------------
name = "Tim"

def hello():
    """Global variables can be accessed from functions."""
    print(f"{hello.__name__} - {name}")

hello()
print(f"{__name__} - {name}")

#----------------------------------
def hello2():
    """Interestingly, we are no longer manipulating here the global variable, name is a local variable,
    the global variable called name stays unchanged!"""
    name = "Tom"
    print(f"{hello2.__name__} - {name}")

hello2()
print(f"{__name__} - {name}")

#----------------------------------
def hello3(name="Michael"):
    """Default parameter value takes over, nothing to do with global name again."""
    print(f"{hello3.__name__} - {name}")

hello3()
print(f"{__name__} - {name}")

#----------------------------------
def hello4():
    """Bring the global variable called name into the local scope, so that it can be changed!"""
    global name
    name = "Patrick"
    print(f"{hello4.__name__} - {name}")

hello4()
print(f"{__name__} - {name}")
