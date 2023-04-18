


# a = complex(10,1)
# b = complex(10,12)
# print(a+b)

# st
str1="abhijit"
# print(str1)

# print(len(str1))
# print(str1[0:-6])
# print(str1[-6:-3])
# print(str1[1:4])
# print(str1[3:6])
# for ch in str1:
# #     prgnt(ch)
# b="!!!!!government Polytechnic Nandurbar!!!!!!!!!"
# print(b.rstrip("i"))
# print(len(b))
# print(b.lower())
# print(b.upper())
# print(b.replace("!","2"))
# print(b.split("t"))
# print(b.split("P"))
# print(b.capitalize())
# print(b.center(130))
# print(b.count("a"))
# print((b.endswith("!!!!")))
# print((b.endswith("bar!!!!")))
# print(b.startswith("!!!!!"))
# print((b.find("!")))
# print((b.find("ment ")))
# print((b.find("223")))
# print(b.index("t",12))
# c="Vedan"
# print(b.istitle())
# print(c.istitle())
# print(b.isalnum())
# print(c.isalnum())
# print(b.isalpha())
# print(c.isalpha())
# print(c.islower())
# print((c.isupper()))
# print(c.isprintable())
# print(b.isprintable())
# d="(/n hi\n hello"
# print(d.isprintable())
# d="hi how Are you"
# print(d.swapcase())
# print(d.title())

# i=4
# match(i):
#     case 5:
#         print("positive 5")
#     case -5:
#         print("negative 5")
#     case 0:
#         print("zero")
#     # case _ if i!=5:
#     #     print("Its nnot 5")
#     # case _ if i==4:
#     #     print("Its 4")
#     case _ :
#         print("none")

# colors = ["red", "orange", "yellow", "pink"]
#
# for i in colors:
#     print(i)
# for a in i:
#     print(a)

# for i in range(0,90,3):
#     print(i)

i=20
# while(i<=100):
#     if(i%2==0):
#         print(i)
#     i+=1

# do while loop
# while(True):
#     print(i)
#     i += 1
#     if(i%100==00):
#         break

# for i in range(40,20,-1):
#     if(i==22):
#        break
#     print(i)

# while(i>=0):
#     i-=1
#
#     if(i==8):
#         continue
#     print(i)


# def ved():
#     pass
# def add(a,b,c):
#     return a+b+c
#
# print(add(10,20,30))

# s={1:"vedant",2:"abhijit",3:"kumar"}
# print(s)


lst= [1,2,3,4,"vedant",6]
#
# if 2 in lst:
#     print("2 is availabel in this list")
# else:
#     print("can't find")
#
# print(lst[len(lst)-3])
# print(lst[-3])
# print(lst[6-3])
#
# print(lst[2:4])
# print(lst[0:-1])
# print(lst[-1])

# print(lst[:])
# print(lst[2:])
# print(lst[0:5:2])

# if "e" in "vedant":
#     print("yes")
#
#
# for a in lst:
#    print(a,end=" ")
#    # for i in a:
#    #     print(i)

# a= [i*i for i in range(10)]
# print(a)
#
# lst = [i * i for i in range(21) if (i % 2 == 0)]
# print(lst)
#
# lst = [i * i for i in range(21) if (i % 2 == 1)]
# print(lst)

l=[1,2,3,4,55,6,4]
# print(l[::-1])
#
# l.append(34)
# print(l)
# l.reverse()
# print(l)
# l.sort()
# print(l)
#
# l.sort(reverse=True)
# print(l)
#
# l.count(4)
# print(l.count(4))
# # l.insert(78)
# print(lst.index("vedant"))
#
# m=l.copy()
# print(m)
# l.extend(lst)
# print(l)
# print(l.pop(2))
# print(l)
# l.remove(55)
# print(l)
# # l.clear()
# l.pop(5)
# print(l)


# tup = (12,True,"vedant",78.098,'c',90)
# a=(1,2,33,4,33,444,4)
#
# print(tup+a)
# print(len(tup))
# print(a.count(33))
# print(a.index(4))
# print(a)

# print("i am vedant {} from dahiwel tal.{} dist . {}".format("bachhav","sakri","dhule"))
#
# a='ved'
# b=34.33333
# c="don"
# l= "hi bros i am {0} my value is {1} and i am {2}"
# print(l.format(a,b,c))
# print(f"i am vedant {a} from dahiwel tal.{b:.2f} dist . {c}")
# print(f"i am vedant {{a}} from dahiwel tal.{b:.2f} dist . {c}")

# def hi(a):
#     # "hello guys i am vedant"
#     'Hello i am vedantt'
#     print(a)
#
# hi(9)
#
# print(hi.__doc__)
#
# import  this

#
# def rec(a):
#     if (a==1 or a==0):
#         return 1
#     else:
#         return (a*rec(a-1))
#
# print(rec(5))
#
# def fib(a):
#     if(a==1):
#         return 1
#     elif(a==0):
#         return 0
#     else:
#         return (fib(a-1)+fib(a-2))
#
# print(fib(10))
# print(fib(5))
# print(fib(6))
# print(fib(7))
# print(fib(8))

# l=[34,343,4,44]
# print(l)
# l.append(233)
# print(l.index(343))
# print(l)
# l.insert(2,44)
# print(l)
# data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
# new_list = []
#
# while data_list:
#     minimum = data_list[0]  # arbitrary number in list
#     for x in data_list:
#         if x < minimum:
#             minimum = x
#     new_list.append(minimum)
#     data_list.remove(minimum)
#
# print (new_list)
#

# REveres array without build in function
# l=[3,5,6,4,7,1,5,6,9]
# k=[]
#
# while l:
#     m=l[0]
#     for x in l:
#         if x<m:
#             m=x
#     k.append(m)
#     # print(k)
#     # print(l)
#     l.remove(m)
#
# print(k)

# l=[8,22,5,6,89,96,698,45,52,2]
# k=[]
#
# while l:
#     m=l[0]
#     for i in l:
#         if(i<m):
#            m=i
#     k.append(m)
#     l.remove(m)

# print(k)
# k.reverse()
# print(k)
#
# print(l))
# #
#
# try:
#     t=(12,34,6,77)
#
#     for a in range(5):
#         i=list(t)
#         i.append(66)
#         i.append(66)
#         t=tuple(i)
#     print(t)
# except :
#     print("check error!!")

marks=[34,34,54,3,32,34,444,433,209]
print(marks[:])
print(marks[:-0])

a= [i+i for i in range(1,11)]
print(a)