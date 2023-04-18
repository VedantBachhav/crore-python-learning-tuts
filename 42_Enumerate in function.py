"""Enumerate function in python : ---> 1) it's built in function in python. 2) it allows to loop over a sequence (
such as list, touple or string) and get the index and value of each element in the sequence at the same time.
3) By default the enumerate function starts the index 0, But you can specify a different string index by passing it as an arguments to the enumerate
function. shown on line no 37"""

marks = [12,25,36,89,59,98,3,1,45]

# without using enumerate function
# index =0
# for i in marks:
#     print(i)
#     if index==5:
#         print("Vedant, awesome!")
#     index +=1






for index, i in enumerate(marks):
    print(f"{i} = {index}")
    if index==5:
        print("Vedant, awesome!")
print()
# for index, i in enumerate(marks, start=3):
#     print(f"{i} = {index}")
#     if index==5:
#         print("Vedant, awesome!")

s= "hello"
for index, c in enumerate(s):
    print(index,c)

print()

# cover point no 3
t= ("apple","banana","mango","santra")
for index, v in enumerate(t,start=1):
    print(index,v)