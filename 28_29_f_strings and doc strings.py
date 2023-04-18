# tut--28 f-string
# f string types
"""
dist="dhule"
d='dahiwel'
name="vedant Devidas Bachhav"
letter="Hi I am {0}. I am from {2} Tal. sakari dist. {1}"
print(letter.format(name,dist,d))

# or f string type

print(f"Hi i am {name} from {d}. Thanks")

#we use as it is don't take this values.
print(f"Hi i am {{name}} from {{d}}. Thanks")


txt = "For only {price: .2f} dollars."
print(txt.format(price =45.25654895))

price=466.96878888
txt = f"For only {price: .2f} dollars."
print(txt)

print(f"{2*30}")
print(type(f"{2*30}"))

print("HI dear i am {} mobile no{}".format("vedant",8007003864))

"""

# tut--29   Doc-string and PEP 8  > Python docstring are the strings literals that appear right after the defination of a function,
# methods, class, of methods.

# def  square(n):
#     '''Takees in a number n, returns the squre of n.'''
#
#
#     print(n**2)
#
# square(7)
# print(square.__doc__)
#
# def  square1(n):
#
#     print(n**2)
#
#     '''Takees in a number n, returns the squre of n.'''
# square1(78)
# print(square1.__doc__)


"""PEP 8 --> 1)PEP stands for Python Enhancement Proposal. 
             2)It provide guidelines and best practices on how to write python code. 
             3)It focus on improve the readability and consistency of python code. 
             4)A PEP is a document that describes new features proposed by python and aspects of python. like design and style for the community. """

# Zen fo python
import  this



