# This is tutorial 31 information about set.
""" 1) Set is collection of well-defined unordered objects.
2) They store multiple items in a single variable.
3) Set items are separated by comma "," and enclosed with {} curly breezes.
4) set are unchangeable, means you can't change items of the set once contained.
5) Set can't contain duplicate items.
6) It can't maintain order.
7) syntax of set and dictionary are same then we use 'c=set()' to print type of empty set.
8) set don't support indexing and slicing because set can't maintain order.
"""

s = {2,3,4,3,6,3,45}
# print(s)  #Values are can't be repeted. refer point 5

# s1= {"vedant",'v',False,'v',34.44,12,345,12}

# print(s1)

# when we print empty set then it shows dict data type
# b={}
# print(type(b))

# then we need to type empty set is given.
# c=set()
# print(type(c))
#
# # a={3,}
# # print(type(a))


'''can't accessing set by given type(indexing) and slicing is also unvalid'''
# print(s1[0]) accessing #refer point 6 run 2-3 times
# print(s1[1])
# print(s1[2])
# print(s1)

# slicing
# print(s1[0:4])
# print(s1[1:4])
# print(s1[4:-1])

""" Accessing set items using for loop"""
#
# for value in s1:
#     print(value)
#
# # iterating using for loop
# a=set("geeks")
# for i in a:
#     print(i)





''' TUT/ Day 32 --> Set Methods and build in functions'''
# build in functions
# **intersection / union means they update the intersections but intersection or union update means they update the set that we will take.
'''
#  1) union --->used for merging two sets and same element print only ones and create different list.

#     update -->  it also adding different element in the mention list.  show line 70 to 74
a={1,2,3,44,5,6}
a1={1,2,13,2,4,55,6}

# a.union(a1)
# print(a,a1)
# print(a.union(a1))
# print(a.union(a1))

# or
# c= a.union(a1)
# print(c)

# a1.update(a) # it also adding different element in the mention list. ex adding a's different element in a1 set like 3, 44 and 5
# print(a,a1)
#
# a.update(a1)
# print(a,a1)



# # 2) Intersection  -->  the values they avilabel in both sets.

c={22,2,34,4,133}
c1={22,12,34,133}

# c2= c.intersection(c1)
# print(c2)
# # or
# print(c1.intersection(c))

#
# c1.intersection_update(c)
# print(c1,c,sep="\n")
# # c.intersection_update(c1)
# # print(c,c1,sep="\n")


# 3) Symentric difference --> means (union - intersection)  its only print the element they are once in a both set
# or it,s not print the element are availabel in both sets (means - intersection elements ) .

# d=c.symmetric_difference((c1))
# print(d)
# # or
# print(c.symmetric_difference((c1)))
#
# a=c.union(c1)
# b=c.intersection(c1)
# print(a-b)


# c.symmetric_difference_update(c1)
# print(c,c1)
# c1.symmetric_difference_update(c)
# print(c,c1)


# 4) Difference and Difference update---> the element are mentioned in both list but not in the reference list then the element is print.eg.
# Reference set is c and mentioned c.difference(c1) then they print the elements they different in c means --> 2 and 4

# d=c.difference(c1)
# print(d)
# # print(c.difference(c1))
# print(c1.difference(c))

c.difference_update(c1)
print(c)
'''

# set methods
n= {"vedant","sani","abhijit",12,2004}
n1= {"ved","sani","abhijit",99,2001}

n2= {"vedant","sani","abhijit",12,2004}
n3= {"ved","nis","abhi",99,2001}
n4={12,2004}

print(n.isdisjoint(n1))#the elements are not repeted in both set. dislike as intersection then it is print false.
print(n2.isdisjoint(n3))

print(n.issuperset(n1)) # when the n1 elements are present in n the it print true another false
print(n.issuperset(n4))

print(n1.issubset(n)) # when the n set store the elements of n1 then it print true another false
print(n4.issubset(n))


n.add(1970)
print(n) # if we want to single element add in a set.

# n.update(n3)
# print(n) # if we want to multiple element or a set add in a set.


n.remove(12)
print(n) # if we want to remove the elemetn in a set.


n.discard(12)
n.discard(1223432)
print(n) # if we want to remove the elemetn in a set but when the element is not present in set then discard can't produce error but remove produce error.


a=n.pop()
print(n)
print(a) # it removes the element randomly (lase element)because set is unordered

# del n3
# print("delete n3 :",n3) # delete n3 set and produce error n3 is not defined.


# print("clear n3 :",n3.clear()) # clearing  n3 set and doesn't produce error.
# print(n3)

if "abhiit" in n:
    print("Yes Boss!!!")
elif "sani" in n:
    print("Yes boss sunny is also in set.")
elif "sanui"in n:
    print("sorry did't match.")