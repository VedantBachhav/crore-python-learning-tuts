"""---- This is tutorial 51----
seek() and tell() functions
1) In Python, the seek() and tell() functions are used to work with fil objects and their positions within a file. These functions are part the built-in io
module, which provides a consistent interface for reading and writing to various file-like objects, such as files, pipes and in-memory buffers.

2) seeK() function.
The seek() function allows you to move the current position within  file to a specific point. The position is specified in bytes, and you move either
forward or backward from the current position.

3) tell() function.
The tell() function returns the current position within th file, in bytes. This can be useful for keeping track of you location within the file
 or for seeking to a specific positin relative to the current position.

4) truncate() function
When you open a file in Python using the open function, you can specify the mode in which you want to open the file. If you specify the mode as
'w' or 'a', the file is opened in write mode and you can write to the file. However, if you want to truncate the file to a specific size, you can use the
truncate function.
"""

with open('a.txt','r')as f:
    print(type(f))
    #values in byes.
    f.seek(10)#  freez or seek the characters we take in seek function argument. suppose we take 10 it will not print with read function first 10 chars

    print(f.tell()) # it shows the how many bytes we seek. it track the position of seek.
    data= f.read(6)# it will read the characters after seek index characters.suppose we take  it will be read after seek  chars.
    print(data)


with open('example.txt','w')as f1:
    f1.write("hello world!")
    f1.truncate(4) #it will take value to how many chars store in file

with open('example.txt','r')as f2:
    print(f2.read())
