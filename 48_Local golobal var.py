"""
About local vs Global variables.
1) what is variable :A variable is a named location in memory that stores a value. In Python, we can assign values to variables using the assignment operator

2)   i)A local variable is a variable that is defined within a function and is only accessible within that function. It is created when the function is called
 and is destroyed when the function returns.
     ii) On the other hand, a global variable is a variable that is defined outside of a function and is accessible from within any function in your code.

3)We can access the value of the global variable x from within the function, but we cannot access the value of the local variable y outside of the function.

+++Global Keyword+++
4) The global keyword is used to declare that a variable is a global variable and should be accessed from the global scope.
5) we used the global keyword to declare that we want to modify the global variable x from within the function. As a result, the value of x is changed to 5.
It's important to note that it's generally considered good practice to avoid modifying global variables from within functions,
 as it can lead to unexpected behavior and make your code harder to debug.
"""
z=90
x=4 # global variable

def hello():
    x=6 # local varialbe
    y=1
    print(z)#it will be print because z is an global varialbe.
    print(f"The local variable is {x}.")

print(f"The global variable is {x}.")

hello()

print(f"The global variable is {x}.")

x=47 #updating global variable
print(f"The updated global variable is {x}.")

# print(y)# it throws error because y is only exist in hello.



def prac():
    global z # updating the value of global variable 99 to 888
    z=888
    print(z)
print(z)
prac()
print(z) # it will be print 888 after running/updating z prac