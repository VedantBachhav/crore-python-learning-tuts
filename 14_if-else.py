# if else --> it is a conditional statement  use condtional operators if condition is true then it evalutes if block statement or
# else condition is false then it evaluetes else block  statements.
# In this statements the space is knowwn as indentation. and it is not use any bracket it use colon and denoted by indentations.


# conditional operators--->   <,> ,<= ,>=, ==, !=
'''
a= int(input("Enter your age \t"))

print(a<18)
print(a>18)
print(a<=18)
print(a>=18)
print(a==18)
print(a!=18)

if a>=18:
    print ("yes")
    print("You are able for voting.")

else:
    print("No")
    print("You are  not able for voting.")
print("Executed!!!")
'''

# elif block
# example
"""
a= int(input("Enter any number : \t"))

if(a==0):
    print("It is a zero number.")
elif a >= 1000:
    print("It is a positive four digit numbers.")
elif a <= -1000:
    print("It is a negative four digit numbers.")
elif a<0:
    print("It is a negative number.")
else:
    print("It is a positive number.")

"""

# Nested if-else block/ statement
# Example


a=int(input("Enter any number \t"))

if(a==0):
    print("It is a zero number.")
elif a>0:
    print("It is a positive number.")
    if a>0 and a<=20:
        print("The number is between 0 to 20.")
    elif a>20 and a<=50:
        print("The number is between 20 to 50.")
        if a>20 and a<=30:
            print("The number is between 20 to 30.")
        else:
            print("The number is greter than 30 and less than 50.")
    else:
        print("The number greter than 50.")
else:
    print("The number is negative.")
print("I am happy.")