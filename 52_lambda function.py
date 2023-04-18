"""Lambda function--> It's a anonymaous function.
1) In Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword.
syntax:lambda arguments: expression
2) Lambda functions are often used in situations where a small function is required for a short period of time. They are commonly used as arguments
to higher-order functions, such as map, filter, and reduce.
3) However, the lambda function is anonymous, as it does not have a name. Lambda functions can have multiple arguments, just like regular functions.
4) the lambda function is anonymous, as it does not have a name.
6) Lambda functions can have multiple arguments, just like regular functions.
7) Lambda functions can also include multiple statements, but they are limited to a single expression.
8) single expression --> Lambda functions are often used in conjunction with higher-order functions, such as map, filter, and reduce which we will look into later.
"""



#  It's a function
# def double(x):
#     return x*2
#
# print(double(5))

def appl(fx,value):
    return 6+fx(value)


# It's a lambda function.
double =lambda x: x*2
cube =lambda x: x*x*x
avgb= lambda x,y: ((x+y)/2)*2+50
if1=lambda x,y: print("x is greater ")  if  x>y else print("Y is greater.")

print(double(5))
print(cube(5))
print(avgb(5,15))
print(if1(12,56))



# taking lambda function to function as argument.
print(appl(lambda x: x*x*x,2))
