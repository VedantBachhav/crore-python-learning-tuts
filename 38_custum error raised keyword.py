"""Raised custom error :
1) In python we can raise custom error by using the raise keyword.
2) we can define custom exceptions by creating a new class that is derived from the built-in exception class.
syntax:
class CustomError(Exception):
    #code.....
    pass
try:
    #code.....
except CustomError:
    #code.....

3) This is useful because sometimes we might want to do something when a particular exception is raised.
4) Example :  Sending an error report to the admin, calling an api, etc.
"""


# Searching some build in execptions on google and implemented on it.
a = int(input("Enter any value between 5 and 9\t"))

if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")

print(a)