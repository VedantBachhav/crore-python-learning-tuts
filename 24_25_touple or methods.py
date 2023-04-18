"""Touple   ---> Touples are immutable we can't changes makes in touple. touples are enclosed with () and seperated by ,(comma)

imp-->line 59"""


tup = (12,True,"vedant",78.098,'c',90)
# # tup[1]=67 # can't print because touples are mutable
# print(type(tup))
# print(tup)

# print(tup[0])
# print(tup[1])
# print(tup[2])
# print(tup[3])
# print(tup[4])
# print(tup[5])

"""Mrthods of finding negative indexing"""
# print(tup[-3]) # Negative index
# print(tup[len(tup)-3]) # Positive index
# print(tup[6-3]) # Positive index
# print(tup[3]) # Positive index


'''finding element using control loops'''
# if True in tup:
#     print("yes")
#
# else :
#     print("no")
#
# # Same thing applied for string as well.
# if "da" in "vedant":
#     print("yes")
# else:
#     print("no")


"""Slicing"""
# tup2=tup[1:4]
# print(tup2)
# tup2=tup[0:-1]
# print(tup2)
# tup2=tup[2:-1]
# print(tup2)

''' Types of printing whole touple.'''

# print(tup)
# print(tup[:])
# print(tup[4:]) #starting from index 4 and goes to -1
# print(tup[-1:])
# print(tup[1:3])
# print(tup[0:-1:2]) # jump index


"""   Tutorial 25 ---> Touple Methods  """

# Touples are immutable but we add or remove elements using list
# eg
'''
countries=("india","russia","usa","chaina","japan","israiel","UAE")
temp=list(countries)
temp.append("Brazil") #Add element
temp.pop(2) #Remove element
temp[4]="Finland"  #change item
temp.insert(5,"ved")
countries=tuple(temp)
print(countries)
'''

# We are merginin to tuples means concanticate two tuples

# t=("vedant","devidas ","bachhav")
# a=(800989998,'mo',True)
#
# ta= t+a
# print(ta)


# inbuild methods in touple ~~~
#
# m =(12,"vedant",True,34.45,12,'v',123,12)
# print(m)

# print(len(m)) #Finding length of touple
#
# a=m.count(12)
# print("The count of 12 is in touple is : ",a) #counting the element how many times repeted in touple

# print(m.m.count(12))

# print(m.index("vedant")) #calculating first occurance of element
# print(m.index(12,2,5)) #syntax = index element occurance (12), start/from(2), end/to(5)



m1=(1,2,[3,4,3])
m=('a','b','c','d','e')
#
"""
# refere from textbook

# built in methods of tuple
print(max(m1))
print(min(m1))

c=zip(m1,m)   # converting into dic form
0
print(list(c))



# membership functions in tuple
# print(2 in m1)
# print(12 in m1)

# if  2 in m1 :
#     print(True)

# Iterating through a tuple
# for i in m1:
#     print(i)


"""


"""
# using list
l=()
j=0
b = int(input("Enter no. of subjects : "))
for i in range(b):
    a=int (input("Enter your marks : "))
    if a<=100:

        t=list(l)
        j += a
        t.append(a)
        l=tuple(t)
    else:
        print("Invalid marks marks less than or equal 100.")

print(l)
print("Sum of marks : ",j)
print("Average : ",j/len(l))
# print(j/b)
"""

# c=zip(m1,m)
# print(list(c))
