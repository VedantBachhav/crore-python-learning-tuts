""" Tut 30--> Recursion in python  ---> 1) Recursion means defining something terms of itself.
2) A functions call other functions. It is even possible for the functions to call itself. These types of construct are termed as recursion functions.
"""
# factorial 7= 7*6*5*4*3*2*1

def factorial(a):
    if (a==1 or a==0):
        return 1
    else:
        return (a * factorial(a-1))

a=17
# print(factorial(a))
# print(factorial(0))



def fibonaachi(a):
    if (a==0):
        return 0
    elif (a==1):
        return 1
    else:
        return (fibonaachi(a-1)+fibonaachi(a-2))

# a=5
print(fibonaachi(0))
print(fibonaachi(1))
print(fibonaachi(8))