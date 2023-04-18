# Tut 11 about string
# String are immutable-->Means it's not change
# String will create in single quote '' or double quote"" both.
# In python a string is  like an array of characters or collection of characters.


# name="Vedant"
# Friend='Kishan'
# print("my name "+name,"my bff "+Friend,sep=" and ")
# print("In python a string is an like an array of characters or collection of characters. Example given below")
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])
# # using loop
# for ch in Friend:
#     print(ch)
# '''Multiline string'''
#
# str= '''He said,
# hello vedant
# I said, "how are you ?"'''
# print(str)
#
# str1= """
# It is a another type of multiline string.
# He said,
# hello vedant
# I said, "how are you ?
# 'Vedant said, \'Hello Amol\''
# abcdefghijklmnopqrstuvwxyz
# """""
# print(str1)
#
# # for ch in str1:
# #     print(ch)
#
# # When we use double or single quote in a string
#
# st= "Vedant said, \"Hello chirag\""
# print(st)
# st1= 'Vedant said, \'Hello Amol\''
# print(st1)
#
# # or
#
#
# a= 'Vedant said, "Hello chirag"'
# print(a)
# a1= "Vedant said, 'Hello Mayur'"
# print(a1)



'''
# Tut 12-->String Slicing and operations on Strings in python

name ="Hello Brother How are you?"

# Slicinginstring.
print(name[0:15])
print(name[5:10])

#negative slicing
f="Mango"
print(f[-5:-3])
print(f[-5:-2])
print(f[-3:-2])

nm="harry"
print(nm[-4:-2])

a=len(name)
print("name strings length is ",a)
'''






# tut 13--> String Methods.
# String are immutable.

b="!!!!!Government Polytechnic Nandurbar!!!!!!!!!"
print(b)

print(len(b))


print(b.upper())

print(b.lower())

print(b.rstrip("!"))#remove all suffix metioned in this function

print(b.replace("Nandurbar", "Dhule"))

print(b.split(" "))
print(b.split("t"))#divided in the form of list from seprated by mentioned in method.

blogheading="introduction to python with Harry. hello bhailog."
print(blogheading.capitalize())# capital 1st letter of blog and other converted to lowercase.
print(len(blogheading))

print(blogheading.center(150)) #alligh sentence in center. Then it gives half number of spaces in suffix part of string.
print(len(blogheading.center(150)))

print(b.count("e"))

print(b.endswith("!!!"))

print(b.endswith("!@!!"))

print(b.endswith("ment",0,15))

str1= "he's name is dhiraj. He is an honest man."

print(str1.find("is"))
print(str1.find("and"))# When keyword does't  mathch with any then it's return -1.

print(str1.index("an"))
# print(str1.index("djflaj"))# When substring is not found then  it produced an error(substring not found error).

str2="12hoursagoA"
str="hoursagoA"
print(str1.isalnum())
print(str2.isalnum())#When A-Z,  a-z  or 1-9 charcters are present then it print true oterwise false.

print(str.isalpha())#When A-Z or a-z charcters are present then it print true oterwise false.

str="Hours Ago\n\tWe go"
print(str.islower())#When all charters are in lower case then it print true anoter false.

print(str2.isprintable())
print(str.isprintable())#When escape sequence charcters are included then it print false.

st="           "
print(st.isspace())#only space required

str="World Health Organization."
print(blogheading.istitle())
print(str.istitle())

print(str.startswith("Wor"))

print(str.swapcase())

str="hello Vedant where from you."
print(str.title())
