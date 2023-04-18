"""Exception Handling-->
 1) Its a process of responding unwanted and unexpected events when a computer program runs.
 2) Its deals with avoiding the program or system crashing".
 3) without this process exceptions disturb the normal operation of a program.
 4) Python has many built in exceptions when your program encounters an error in try block then interpretor stops the current process and passing
  to the calling process until it is handled . If not handles then program will be crash .
 5) except block shows/throws an error, we defined sepecific built in exception also like ValueError,InexError,etc.   """


try:
    a = int(input("Enter no.\t"))
    print(f"Multiplication table of {a} is given : \n")
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a*i)}")
except:
    print("Invalid Input!!")

print("Some IMPORTANT Lines of code.")
print("End of program.")




# try:
#     num = int(input("Enter number: "))
#     a=[6,3]
#     print(a[num])
#
# except ValueError:
#     print("Number entered is not an integer")
# except IndexError:
#     print("Invalid Index !!")