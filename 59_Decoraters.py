"""
Decorators in python.
There are two ways to define decorators in program.
I) using @decorator_function_name
II) using decorator_function_name(fuction_for decorating_name)()

1) decorators are the function that change the function and return.



"""

def greet(fx):
    def mfx(*a,**b):
        print("hello sir..")
        fx(*a,**b)
        print("Thanks for using this function.",end="\n\n")
    return mfx


@greet
def hello1():
    print("hello world.")

@greet
def hey():
    a=input("enter your name")
    print("Your name is : ",a)
@greet
def add (a,b):
    print(a+b)



hello1()
# add(10,12)
hey()
greet(hello1)()
# greet(add)(12,25)





# example:
"""
def hello(fx):
    def mfx():
        print("hello pari")
        fx()
        print("good bye pari\n\n")
    return mfx


@hello
def ved():
    print("me vedant bachhav aahe")


ved()

@hello
def ved1():
    print("me vedant Devidas bachhav aahe")


ved1()
    
"""