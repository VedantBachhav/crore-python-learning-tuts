# Tutorial 4 ----> first program line by line
import sys

print("hello world!")  #print is an a function. Function is use for performing some task.
print(4)                #() it is parenthesis used for invoking function.
print(4*60)       #"" it is used for printing string. when you not enterd valid object then used "".
print(4*60, 20+6, "vedant")  # using , (comma) we taking multiple values in a function or in a single line.



# Tutorial 5 -----> Comment, Escape sequences and print statements

"""comments"""

# hash is used fo single line comment.


'''hello 
vedant 
devidas
bachha'''

"""hello 
vedant 
devidas
bachha"""

#'''  3 quote is used for multiline comment or we use double quote also """

"""Escape sequences characters"""

# You cannot character insert directly used in a string, we use an escape sequence character and this char is / blackslash.

"""
\n--> used for new line
\"--> used for used double or single quote in string.
\t--> used for extra space in string means tab.
"""

print("Hello world\nvedant you are my friend.")
print("Hello world \"vedant\" you are my friend.")
print("Hello world\t\tvedant you are my friend.")



"""Print statements"""
# , comma is used for write new element with string element ,we shown in example.
# sep is used for sepration in joint string element ,we shown in example.
# end is used for print an element in end of line / string ,we shown in example thanks print an end of line.
# sep or file is an optional .
# *file an object with a write method . default is sys.stdout (note : this will be explained in upcoming tutorial. )

print("This is python tutorial playlist.",100,"Videos in this playlist.", sep="_", end="Thanks.\n")
print("This is python tutorial playlist.",100,"Videos in this playlist.", sep=" ", end="009")\


