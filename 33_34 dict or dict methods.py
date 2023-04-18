# this is tutorial / day no 35 and 3
"""
1) Dictonary are ordered collection of data items.
2) It is used to creating a mapping.
3) They store multiple items in a single variable.
4) Dict items are key: value pair, they seperated by "," comma and enclosed by curly brases{}.
"""
a={1:"patil",2:"india",3:"dahiwel",4:"vedant",5:"dahiwel",6:"sakri"}
b={'a': 2343,
   'z':78,
   'c':7890,
   'd':1112}

# print(type(a))
# print(type(b))

"""Accessing a single value in a dict."""
# print(a[1])
# print(a[5])
# print(b['a'])
#
# print(b['d'])
# print(b.get('d'))
# # print(b['d1']) # when the key is not availbel then it produce error.
# print(b.get('d1'))# when the key is not availbel then it not  produce error and show none.


"""Accessing a multiple values and keys in a dict. or using loops"""

# print(a.keys())
# print(b.keys())
# print(a.values())
# print(b.values())
# # printing whole dict.
# print(a)
# print(b)

#  accessing the keys using loops

# for i in b.keys():
#    print(i)
#
# for i in a.values():
#    print(i)
#
# for i in a.keys():
#    print(f"The values corresponding to the key {i} is {a[i]}.")

# accessing key value pair.
# print(a.items())
# for key, value in a.items():
#    print(f"The key is {key} and its value is {value}")


# day 34 ---->dict methods.


# a.update(b)# adding dict b elemtents in a
# print(a)

# b.clear() # deleting all element from b but not produce error and print none
# print(b)

# a.pop(2) # deleting one element form dict
# print(a)

a.popitem() # deleting last element form dict
print(a)

# del a  # deleting all element from a and thrown error when we trying to print undefiend variable
# del a[3]  # deleting 3rd index element from a
# print(a)

c= a.copy() # copying element in c from a.
print(c)

a.setdefault(7,"dadu") # retruns the value of the specified key. if the key does't exist insert the key with the specified values.
print(a)

# a= a.fromkeys(["dahiwel","sakri","dhule"],"village") # it creates sperate list  multiple values with single key
# print(a)
# print(a.get("sakri"))
#
# # c= c.fromkeys(["dahiwel","sakri","dhule"],"village",[12,23,4,65,67],1)
# # print(c)

# print(b.get('d'))
'''key, values , items and get are also methods of dict.'''

c={}
# built in functions
print(all(a))
print(all(c)) # returns true when any element or empty dict.
print(any(c)) # returns true when dict is  empty.
print(any(b)) # returns true when dict is  empty.
print(type(a))
print(len(a))
print(sorted(b))