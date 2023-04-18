"""
Introduction to Object-oriented programming

Introduction to Object-Oriented Programming in Python: In programming languages, mainly there are two approaches that
are used to write program or code.

• 1). Procedural Programming

• 2). Object-Oriented Programming

I) The procedure we are following till now is the "Procedural Programming" approach. So, in this session, we will learn
about Object Oriented Programming (OOP). The basic idea of object-oriented programming (OOP) in Python is to use
classes and objects to represent real-world concepts and entities.

II) A class is a blueprint or template for creating objects. It defines the properties and methods that an object of that
class will have. Properties are the data or state of an object, and methods are the actions or behaviors that an
object can perform.

III) An object is an instance of a class, and it contains its own data and methods. For example, you could create a
class called "Person" that has properties such as name and age, and methods such as speak() and walk(). Each instance
of the Person class would be a unique object with its own name and age, but they would all have the same methods to
speak and walk.

IV) One of the key features of OOP in Python is encapsulation, which means that the internal state of an object is
hidden and can only be accessed or modified through the object's methods. This helps to protect the object's data and
prevent it from being modified in unexpected ways.

v) Another key feature of OOP in Python is inheritance, which allows new classes to be created that inherit the
properties and methods of an existing class. This allows for code reuse and makes it easy to create new classes that
have similar functionality to existing classes.

VI) Polymorphism is also supported in Python, which means that objects of different classes can be treated as if they
were objects of a common class. This allows for greater flexibility in code and makes it easier to write code that
can work with multiple types of objects.

In summary, OOP in Python allows developers to model real-world concepts and entities using classes and objects,
encapsulate data, reuse code through inheritance, and write more flexible code through polymorphism.

"""
#
# class Solution(object):
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         num=0
#         if(x<0):
#             while x<0:
#                 n=x%-10
#                 num=num*10+n
#                 x=int(x/10)
#             print(num)
#         else:
#             while x > 0:
#                 n = x % 10
#                 num = num * 10 + n
#                 x = int(x / 10)
#             print(num)
# a = Solution()
# a.reverse(123)
# a.reverse(-123)
# a.reverse(120)
#29
# class Solution(object):
#     def divide(self, dividend, divisor):
#         """
#         :type dividend: int
#         :type divisor: int
#         :rtype: int
#         """
#
#         c = int(dividend / divisor)
#         return c
#
# a = Solution()
# print(a.divide(10,3))
# print(a.divide(7,-3))

