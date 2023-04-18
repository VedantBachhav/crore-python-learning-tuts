""" # function useed for seperating code or used repetedly
There are two types of function used in python.
1)  user difiend function ---> In this function we can never use 'def' keyword or it is made by programmer or user.
eg. given below build by user.
syntax --> def function_name(parameters):
              pass
              # code and syntax
1)  Built-in function ---> In this function we can't'  use 'def' keyword or it is in bulit in python interpreter.
eg. print(), min(), add(), touple(),etc."""


def gmean(a,b):
    print((a * b) / (a + b))
    # return (a * b) / (a + b)

# print(gmean(1,2))#using return
gmean(132,23)
gmean(12,2)


def lessnum(a,b):
    if(a<b):
        print(a, "is  less number than ",b,sep=("  "))
    else:
        print(b, "is  less number than ",a,sep=("  "))


def greaternum(a,b):
    if(a>b):
        print(a, "is  greater number than ",b,sep=("  "))
    else:
        print(b, "is  greater number than ",a,sep=("  "))

greaternum(123,433)
greaternum(12,3)
greaternum(13,3)
greaternum(13,43)

lessnum(123,4)
lessnum(23,48)
lessnum(12,988)
'''
def k():
    a = int(input("Enter first number \t"))
    b = int(input("Enter second number \t"))

    print("addition of a  and b = is ",(a+b))

    c=input("Are you want continue yes or no\t")

    if(c== 'Yes'):
        k()
    elif (c == 'yes'):
        k()
    else:
        print("Thank you!!")
k()'''
def empfunc(a,b):
    pass
# pass is used for when we want to work on this function later then we pass and compiler cant show error.
# simple words empty function.



print("done")