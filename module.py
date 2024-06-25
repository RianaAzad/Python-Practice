import matplotlib


# Use virtual environment while downloading/installing modules. 
'''Global Environment vs. Virtual Environment
Global Environment
Global Environment: This is the default environment where Python and its packages are installed. When you install a package globally using pip, it becomes available system-wide.
Conflicts: Installing packages globally can lead to conflicts between different projects. For instance, if two projects require different versions of the same package, installing one version globally can break the other project.
Virtual Environment
Virtual Environment: This is an isolated environment that allows you to install packages locally to a specific project without affecting the global Python environment or other projects.
Isolation: Each virtual environment has its own site-packages directory, which means you can have different versions of the same package in different environments.
Dependencies Management: Using virtual environments helps manage dependencies more effectively and ensures that each project has the required packages in the correct versions.

'''

import random 

# for i in range (10):
    # print(random.randint(1, 25))

from random import randint

# for i in range (5):
#     print(randint(2,30))

import math as m
import matplotlib.pyplot as plt

print(m.pi)

'''
************* Concept ********
               Module
A module is a file containing Python code that defines functions, classes, and variables. Modules allow you to organize your code into manageable sections and reuse code across multiple programs.

Creating a Module: Any Python file (e.g., mymodule.py) can be treated as a module.
Using a Module: Modules can be imported into other Python programs using the import statement.

               Import
The import statement is used to bring in modules and their functionalities into your current script. It allows you to access functions, classes, and variables defined in the module.


             Statement
A statement is an instruction that the Python interpreter can execute. It can perform actions such as creating variables, calling functions, or controlling the flow of execution.
'''