"""
Short hand if else :--> If else in one line
1) there is also a shorthand syntax for the if-else statement that can be used when the condition being tested is simple and
the code blocks to be executed are short.
2) It's the convenient way to write simple if-else statements, especially when to assign a value to a variable based on condition.
3)It's not suitable for more complex situations where you need multiple statements or perform more complex logic.
"""

a= 5001
b=500
print("A") if a > b else print("=") if a==b else print("B")

print(9) if a>b else ""

c= 90 if a>b else 0
print(c)
c= 90 if a<b else False
# c= 90 if a<b else 0
print(c)

