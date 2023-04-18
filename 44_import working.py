"""
1) Importing in Python is the process of loading code from a Python module into the current script. This allows you to use the functions and variables defined
in the module in your current script, as well as any additional modules that the imported module may depend on.
2)To import a module in Python, you use the import statement followed by the name of the module. For example, to import the math module,
which contains a variety of mathematical functions, you would use the following statement:
import math
3) Once a module is imported, you can use any of the functions and variables defined in the module by using the dot notation.
For example, to use the sqrt function from the math module, you would write:
import math

result = math.sqrt(9)

print(result) # Output: 3.6

4))from keyword

You can also import specific functions or variables from a module using the from keyword. For example, to import only the sqrt function from the math module,
you would write: eg shwon below

5) importing everything
It's also possible to import all functions and variables from a module using the wildcard. However, this is generally not recommended as it can lead to
 confusion and make it harder to understand where specific functions and variables are coming from.
from math import or form math import * both are working
result = sqrt(9)
print(result) Output: 3:0
print(pt)

Output: 3/141592653589793
6) Python also allows you to rename imported modules using the as keyword. This can be useful if you want to use a shorter or more descriptive name for a
module, or if you want to avoid naming conflicts with other modules or variables in your code.
"""


# import pandas
#
# pandas.read_csv()

import math

import imports

b=math.sqrt(16)
print(b)
print(math.floor(12.25689))
print(math.pi)


"""Using from keyword"""

from math import sqrt,pi
#using from keyword we don't need to use "math." we directly use imported function.
print(pi)

b=sqrt(16)
print(b)

"""Using from keyword or *"""

from math import *# not recommended because in our program all functions or scripts are imported .

#using from keyword we don't need to use "math." we directly use all function. It is use when module name is long or complex.
b=sqrt(16)*pi
print(b)

"""Using as keyword."""
# in As keyword we take rename or change the name of library or package.
import  math as m

from  math import pi,sqrt as s

print(s(81),m.pi)

b=m.factorial(5)
print(b)


"""Used dir function."""
# It is used for shown all functions or variables in the specific library.

# import math
# import numpy
# a=dir(math)
# print(a)
# # c="s"
# # print(c.center(160,"_"))
# print(dir(numpy))
print(type(math.pi))# for showing type of fucntion

from imports import * # it imports functions or variable from imports file that is made by me

vedant()
print(a)
print(dir(imports))

