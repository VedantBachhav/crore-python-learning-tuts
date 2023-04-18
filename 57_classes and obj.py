"""
Python Class and Objects

A class is a blueprint or a template for creating objects, providing initial values for state (member variables or
attributes), and implementations of behavior (member functions or methods). The user-defined objects are created
using the class keyword.


Syntax:
class class_name:
    # methods , variable, keywords
    # block of code

Let us now create a class using the class keyword.

class Details:

    name = "Rohan"
    age = 20

Creating an Object:

Object is the instance of the class used to access the properties of the class Now lets create an obiect of the class.

syntax :
object_name = class_name()

"""


class person:
    name = "vedant"
    occuupation = "developer"
    networth = 10

    def info(self):
        print(f"{self.name} is an {self.occuupation}.")
# self parameter is an current instance of the class, and it's used to access variable that belongs to the class.
a= person()

print(a.name, a.occuupation, a.networth, sep="     ", end="\n ")

a.name= "abhi"
a.occuupation= "tester"
a.networth=25
print(a.name, a.occuupation, a.networth, sep="     ",end="\n")

b=person()
b.name= "sani"
b.occuupation = "HR"
b.networth = 1200
#  self ka matlab jispe ye method call ho raha hai, jais ki a pe kiya to a or b pe kiya to b ki information.
a.info()
b.info()