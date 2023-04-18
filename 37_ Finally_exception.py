
"""Finally block
1) It's a part of exception handling.
2) When we handle exception using the try and catch block we can include a finally block at the end.
3) It's alwoays executed, so it is generally used for bulilding the concluding tasks like closing file resources or closing database connection or
may be ending the program executon with a delightful messasge.
4) one of the important use of finally block is in a function which returns a value.
syntax:
try :
    #Statement which coud generated
    #exception
except:
    #Solution of generated exception.
finally:
    #block of code which is goint to execute in any situation.
"""

# l=[23,34,23,58,89,96]
# try:
#     n = int(input("Enter index of list : "))
#     print(l[n])
# except:
#     print("Enter valid input!!")
#
# finally:
#     print("It will be always executed !!")
#
# # print("but we will done with like this also")

#Example of point number 4
def practise():
    l = [23, 34, 23, 58, 89, 96]
    try:
        n = int(input("Enter index of list : "))
        print(l[n])
        return 1
    except:
        print("Enter valid input!!")
        return 0

    finally: # it will always executed whether value return or not.
        print("It will be always executed !!")

    # print("with this technique it will not be executed because value return is not return in this blcok")

a=practise()