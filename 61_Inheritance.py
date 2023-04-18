"""
 ---------- Inheritance in python  ----------
 Inheritance is an object-oriented programming concept that allows one class to inherit the
properties and methods of another class. In Python, there are three types of inheritance:

Types of inheritance : 1) Single Inheritance: In single inheritance, a derived class inherits from a single base
class. The derived class can access all the non-private properties and methods of the base class.

 2) Multiple Inheritance: In multiple inheritance, a derived class inherits from two or more base classes. The derived
 class can access all the non-private properties and methods of all the base classes.

3)Multi-level Inheritance: In multi-level inheritance, a derived class inherits from a base class, and another
derived class inherits from the first derived class. The second derived class can access all the non-private
properties and methods of both the base class and the first derived class.

4) Hierarchical Inheritance : is a type of inheritance in which a single parent class has multiple child classes. In
this type of inheritance, the child classes inherit properties and methods from a common parent class. Each child
class can add its own properties and methods in addition to those inherited from the parent class.

"""

# Single inheritance
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# class Employee(Person):
#     def __init__(self, name, age, salary):
#         super().__init__(name, age)
#         self.salary = salary
#
# emp = Employee("John", 30, 5000)
# print(emp.name)     # Output: John
# print(emp.age)      # Output: 30
# print(emp.salary)   # Output: 5000
#
#
# # Multipal inheritance
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# class Employee:
#     def __init__(self, salary):
#         self.salary = salary
#
# class Manager(Person, Employee):
#     def __init__(self, name, age, salary):
#         Person.__init__(self, name, age)
#         Employee.__init__(self, salary)
#
# mgr = Manager("John", 30, 5000)
# print(mgr.name)     # Output: John
# print(mgr.age)      # Output: 30
# print(mgr.salary)   # Output: 5000
#
# # Mulitlevel Inheritance
# class Animal:
#     def __init__(self, species):
#         self.species = species
#
# class Mammal(Animal):
#     def __init__(self, species, name):
#         super().__init__(species)
#         self.name = name
#
# class Dog(Mammal):
#     def __init__(self, name, breed):
#         super().__init__("Dog", name)
#         self.breed = breed
#
# my_dog = Dog("Rufus", "Golden Retriever")
# print(my_dog.species)   # Output: Dog
# print(my_dog.name)      # Output: Rufus
# print(my_dog.breed)     # Output: Golden Retriever
#
#
# # Hierarchical Inheritance
#
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print("An animal makes a sound")
#
#
# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def speak(self):
#         print("Woof!")
#
#
# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def speak(self):
#         print("Meow!")
#
#
# class Horse(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def speak(self):
#         print("Neigh!")
#
#
# dog = Dog("Fido")
# cat = Cat("Fluffy")
# horse = Horse("Silver")
#
# dog.speak()  # Output: Woof!
# cat.speak()  # Output: Meow!
# horse.speak()  # Output: Neigh!




class a:
    def n(name):
        print("your hgjhname ",name)
class b (a):
    def n(age):

        print("your age",age)

d=b()
# c=a()
# d.name="veda/

d.n("dant")
d.n("ved")