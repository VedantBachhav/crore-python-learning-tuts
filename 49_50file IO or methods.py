""" tut 49 here and tut50 is below
File Input/Output :
1) Before we can perform any operations on a file, we must first open it. Python provides the open) function to open a file. It takes two arguments :
 the name of the file and the mode in which the file should be opened. The mode can be 'Y' for reading, 'w for writing, or "a' for appending.
2) By default, the open() function returns a file object that can be used to read from or write to the file, depending on the mode.
3) Modes in file

There are various modes in which we can open files.

1. read(): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter

2. write (w): This mode opens the file for writing only and creates a new file if the file does not exist.

3. append(a): This mode opens the file for appending only and creates a new file if the file does not exist.
"""

# _______________________Tutorial 49______________________________
"1) Read mode()"
# f=open("data/t.txt",'r')#"r" is an default mode also.
# # print(f)
# t=f.read()
# print(t)
# f.close()


"2) Write mode(w)"
# f1=open("data/t.txt",'w')
# f2=open("data/tt1.txt",'w') # it creates new file when file is not exist in our system.
# t=f2.write("Hello") # It will be write text into given file.
# # t=f1.write("Hello") # It will be write text into given file but it will be overloop the text. means erase previous text and append new text.
# f2.close()

# f3=open("data/a.txt", 'w')
# f3.write("hello baba")
# f3.close()


"3) Append mode(a)" # It includes text in file withour overlapping at the end.

# f1=open("data/t.txt",'a')
# t=f1.("hello")
# f1.close()

# try:
#     # Open a file in append mode ('a')
#     file = open("data/a.txt", "a")
#
#     # Write some data to the file
#     file.write("\nThis text will be appended to the end of the file.")
#
#     # Close the file
#     file.close()
#
#     print("File appended successfully.")
#
# except Exception as e:
#     print("An error occurred: ", str(e))


"4) Create mode(x)" # it will be create file but file is exist then it will be thrown error.
'''
try:
    # Open a file in create mode ('x')
    file = open("example.txt", "x")

    # Write some data to the file
    file.write("Hello, world!")

    # Close the file
    file.close()

    print("File created successfully.")

except FileExistsError:
    print("File already exists. Cannot create a new file with the same name.")

except Exception as e:
    print("An error occurred: ", str(e))
'''


"5) Text mode(t)"#It will be open file in text mode.

#Reading a file
# f1 = open("data/t.txt", 'rt')
# t=f1.read()
# print(t)
# f1.close()

# Writing a file


"6) Binary mode(b)"#It will be open file in binary mode.

#Reading a file
# f1 = open("data/t.txt", 'rb')
# t=f1.read()
# print(t)
# f1.close()


# #Writing a file
# a1=int(input("no. of lines :\n"))
# f1 = open("data/a.txt", 'a')
# for i in range(a1):
#     a = input('Enter text :\n')
#     f1.write("\n"+a)
# f1.close()



#when we use with keyword we don't need to close the file.
# with open("data/t.txt", 'rb'):
#     t=f1.read()
#     print(t)


# ________________________Tutorial 50 -->Rochak methods______________________________
#readline
# a=open('data/a.txt','r')
# while True:
#     l=a.readline()#it will be read file by line by line. it will be use in some case when we seprated the marks,etc.
#     print(l)
#     if not l:
#         print(l, type(l))
#         break

#writelines
# a=open('data/a.txt','w')
# l=['line1\n','line2\n','line3\n']
# a.writelines(l) # write in file like iterable object or lines. lines seperate user ko karna padega nahi to loop lagana padega so use write.
# a.close()