# loops --> Execution a group of statements in a certain numbers of times this can done using loop.
#  do while loop does't use in python.
"""for loop"""

# range(start,end,step)

# a = input("Enter name : ")
#
# for i in a:
#     print(i)
#     if( i=='b'):
#         print("B is something special")                 
#

# colors = ["red","orange","yellow","pink"]
# for x in colors:
#     print(x,end=','"\n")
#     for i in x:
#         print(i)

# for l in range(0,30,2):
#     print(l)


#     odd numbers

# for i in range(0,30):
#     if(i%2==1):
#         print(i)

        # or using range
# for i in range(1,30,2):
#     print(i)


# for k in range(0,35):
#     if(k%2==1):
#         print(k+1)



""" While loop"""

# i=0
# while i<=4:
#     print(i)
#     i+= 1
#
#
# a= int(input("Enter the number"))

# while a<=100:
#     a=int(input("Enter the number again less than 100 : "))
#     print(a)
# print("Thanks!!!")




# Decremental while loop
#
# while a>0:
#     print(a)
#     a -= 1
# else:
#     print("I am inside else.")




# do while loop is not supported by python but we immulate by infinite while loop
# Do while is a loop its a set of intstruction  will the execute at least once.


# i=0
#
# while(True):
#     print(i)
#     i+=1
#     if(i%10==00):
#         break


"""day 35---> else with loops"""

# without break it never returns else (most of the cases.)

for i in range(6):
    print(i)
else:
    print("sorry i")

# i =0
#
# while i<=12:
#     print(i)
#     i+=1
# else:
#     print("sorry i hmm")


# with break it doesn't return else

# for i in range(6):
#     print(i)
#     if(i==4):
#         break
# else:
#     print("sorry i")
#
# i =0
#
# while i<=12:
#     i += 1
#     print(i)
#     if (i == 9):
#         break
#
# else:
#     print("sorry i hmm")


