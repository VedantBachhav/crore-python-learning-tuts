# t= ['vedant',45,"hello world", 56.78]
# print (t)
# print(type(t))
# l=(12,34,56,78,88,'vedant',45,"hello world", 56.78)
# print(l)
# print(type(l))

''' This is tutorial 22
List --> i)   list is a ordered collection of data in python.
         ii)  They store multiple items in a single varialbe.
         iii) List items seperated by a comma and enclosed by a square bracket.[]
         iv)  List is changeble  means mutable.
        '''

marks = [3, 4, 5, 6, "vedant", True]  # include different data types .

# # marks[0]=5
# print(type(marks))
# print(len(marks))
# print(marks)
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])


"Indexing negative -3"

# print(marks[-3]) # Negative index
# print(marks[len(marks)-3]) # Positive index
# print(marks[6-3]) # Positive index
# print(marks[3]) # Positive index
#
# print(marks[-4])
# print(marks[len(marks)-4])
# print(marks[6-4])
# print(marks[2])
#

'''Slicing'''
# print(marks[::-1]) # print in reverse order
# print(marks[-1:0:-1]) # print in reverse order
# print(marks[1:4])
# print(marks[0:-1])
# print(marks[2:-2])

'''finding element using control loops'''
# if "vedant" in marks:
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


''' Types of printing whole list.'''

# print(marks)
# print(marks[:])
# print(marks[4:]) #starting from index 4 and goes to -1
# print(marks[-1:])
# print(marks[1:3])
# print(marks[0:-1:2])#jump index


''' List comprehension'''

# Syntax ---> variable = [Expression for variable/item in iterable(range) if condition]

# lst = [i for i in range(4)]
# print(lst)
#
# lst = [i * i for i in range(21)]
# print(lst)
# # using condition
# lst = [i * i for i in range(21) if (i % 2 == 0)]
# print(lst)
#
# # using condition
# lst = [i * i for i in range(21) if (i % 2 == 1)]
# print(lst)
#
# lst = [i + i for i in range(21)]
# print(lst)
#
# list = [i *i* i for i in range(21)]
# print(list)
'''
l=[]
j=0
b = int(input("Enter no. of subjects : "))
for i in range(b):
    a=int (input("Enter your marks : "))
    if a<=100:
        j += a
        l.append(a)
    else:
        print("Invalid marks marks less than or equal 100.")



print(l)
print("Sum of marks : ",j)
print("Average : ",j/len(l))
# print(j/b)

'''

"""tutorial 23 ---> List methods """

l= [445,56,67,78,56,88]
# print(l)

# l.append(44)
# l.append(56)
# print(l)

# l.reverse()#printing original string in reverse order.
# print(l)
#
# l.sort()
# print(l)
#
# l.sort(reverse=True)
# print(l)

# print(l.index(78)) #printing position of number.
#
# print(l.count(56)) # Counting given number repeted time.

# m=l.copy() # coopying list into m
# m[0]=0
# print(m)
# print(l)

# l.insert(1,909) # inserting element at index 1 position.
# print(l)

# m=[i*i for i in range(2,8)]
# print(m)
# l.extend(m) # extending list (concanicate with l)
# print(l)

# or 2nd concanicate method

# k= m+l
# print(k)

# l.clear()# remove all elements
# print(l)

# l.remove(67) # remove specific element
# print(l)
#
# l.pop(5) # deleting index no element
# print(l)
#
# print(len(l)) # finding length of list.





"""
# Refer from textbook

lst1 = [[1,2,3,4,5],['a','b','c','d','e'],['#','%','&','@']]
lst= [123,34,64,67,879,175]
print(lst1)

#Traversing  a list
# for i in lst1:
#     for j in i:
#         print(j,end=" ")
#     print()


# Built in functions in a list
print(len(lst1))
print(max(lst))
print(min(lst))
print(sum(lst))

# print(lst(seq))
l=list(lst)
print(l)# used in touple for converting a touple

"""