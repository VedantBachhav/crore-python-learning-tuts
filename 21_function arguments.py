# function useed for seperating code or used repetdily
# return is a calling function
'''There are four types are arguments provided by python.
1) default argument. It assumes a default value if a value is not provided in the function call for that argument.
2) Keyword argument. This allows us to skip arguments or place them out of order because the Python interpreter is able to use the keywords provided to match the value with paremeter.
3) Variable length argument. In many cases we required  to process a function with more no of argument than we specified in the function defination.
4) Required argument. Arguments passed to a funtion in correct positional order. Here the no. of arguments in the function match exactly with the function defination.
'''

# 1) default argument example
# def avg(a=90,b=98):
#     #print("Average is ",(a+b)/2)
#     return (a+b)/2 # means is value ke leke vapas chale jao
# print(avg())#for return statement
# avg(34)# taking a value and used default b value
# avg(22,56)# ignoring the 90 and 98 and take this values

# or
# def avg():
#     print("hello")
# avg()
# or

def avg(a,b=2):
    return a+b
print(avg(3))

# 2) keyword argument example
#
# def avg(a,d):#In this function we pass argumentas as a key =value order is not neccessary. This means interrpreter recognize the argument by parameters name.
#     print("Average is ",(a+b)/3)
# avg(d=67,a=89)

# 3) Variable length argument.

# def avg(*numbers): # numbers is itterable keyword and taking as a touple(* is used for including in touple)
#     print(type(numbers))
#     avg=0
#     for i in numbers:
#         avg= avg+i
#     print("length of numbers is ",len(numbers))
#     print("sum of numbers is ",avg)
#     print("Average is ", avg/len(numbers))
#
# avg(12,23,23)
# avg(22,23)
# avg(22,34,45,65,76,5,6,777,755,423,67,999,89,3)

#
# def name(**name):#(** is used for including in dictionary) taking input as a dict
#     print(type(name))
#     print("hello",name["fname"],name["mname"],name["lname"],name["no"])
#
#
# name(lname="Bachhav",fname="Vedant",mname="Devidas",no="8007003864")




# 4) Required argument example
# def avg(a,b):#  a is a required value and b is optional
#     print("Average is ",(a+b)/2)
# avg(45)
#
# def avg(a,c,b):#  all are a required value s
#     print("Average is ",(a+b+c)/3)
# avg(23,34)

