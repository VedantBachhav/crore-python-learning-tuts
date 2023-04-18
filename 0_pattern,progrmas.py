
a = int(input("Enter a number : \t"))


"""Armstrong Numbers"""
# num=a
# sum=0
# while (a>0):
#     rem=a%10
#     sum=sum+rem*rem*rem
#     a=int(a/10)
# if num==sum:
#     print(num," is armstrong")
# else:
#     print(num, " is not armstrong")


"""Sum of digit of given numbers"""
# sum=0
# while a>0:
#     rem=a%10
#     # print(rem)
#     sum=sum+rem
#     a=int(a/10)
#     # print(a)
# print("Sum of number = ",sum)


"""Find out the reverse of the number."""
# rev=0
# while a>0:
#     rem=a%10
#     print(rem)
#     rev=rev*10+rem
#     print("hello",rev)
#     a=int(a/10)
#     print("Hi",a)
# print("Reverse of number = ",rev)


"""Enterd number is prime number or not."""
# for i in range(1,a+1):
#
#     if a%i==0:
#         break
# if i==a:
#     print(a," is a prime number.")
# else:
#     print(a," is not a prime number.")


"""Fibonachi series"""
# x=0
# y=1
# z=2
# print("Fibonachi sequence is : ")
# print(x)
# print(y)
# while(z<a):
#     z=x+y
#     print(z)
#     x=y
#     y=z
#     z+=1




"""Factorail of n numbers"""
#fact =1
# if a<0:
#     print("Sorry, Negative numbers doesn't exist.")
# elif a==0:
#     print(0)
# elif a==1:
#     print(1)
# else:
#     for i in range(1,a+1):
#         fact=fact*i
#         print(fact)


"""# for printing 1,22,333"""
# for i in range(a):
#     for j in range(i+1):
#         print(i,end=" ") # for printing 1,22,333
#         # print(j,end=" ")# for printing 0,01,012
#     print()



# for i in range(0,a+1):
#     for j in range(i+1):
#         print("*",end="  ")
#     print()



for i in range(a,0):
    for j in range(i-1):
        print("#",end=" ")
    print()


"""For pyramid amazing"""
# for row in range (1,a):
#     for sp in range(1,a-row):
#         print(' ',end=" ")
#     for col in range(1,row+1):
#         print(col,end=" ")
#     for i in range (col-1,0,-1):
#         print(i,end=" ")
#     print()


""" # pyramid using counter like 1,2,3,4,1,2,3,4,1."""
# count=1
# for i in range(a):
#     for j in range(i+1):
#         print(count,end="  ")
#         count = count + 1
#         if count>9:
#             count =1
#     print()


# count=1 # pyramid using counter.
# for i in range(a):
#     for j in range(i+1):
#         print(count,end="  ")
#         count = count + 1
#     print()


'''Pyramid using while loop.'''
# i=1
# while (i<a):
#     j=1
#     while j<(i+1):
#         print("@",end=" ")
#         j=j+1
#     i=i+1
#     print()




# import calendar
# yy=2023
# mm=4
# print(calendar.month(yy,mm))
#