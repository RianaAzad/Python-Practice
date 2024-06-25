# Global variable
x = 10

def modify_global():
    global x  # Declare x as global
    x = 20  # Modify global variable

print(x)  # Output: 10
modify_global()
print(x)  # Output: 20


'''
What is a Global Variable?
A global variable is a variable that is defined outside of any function or class and is accessible throughout the entire module. In other words, global variables can be read and modified from any part of the code.

Defining and Using Global Variables
Global variables are defined at the top level of a script or module, outside of any function or class.
'''