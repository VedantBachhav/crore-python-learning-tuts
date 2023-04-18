# It is a built-in module in python
# refer all moduls with example---->
""" https://www.javatpoint.com/python-os-module"""
import os
# for i in range(0,100):
#     # os.mkdir(f"data/tutorial{i}.py")
#     os.rename(f"data/tutorial{i}.py",f"data/tutorial{i}")

print(os.name)

print(os.getcwd())     #It returns the current working directory(CWD) of the file.

print(os.chdir("C:\\"))  #The os module provides the chdir() function to change the current working directory.

os.rmdir("d:\\newdir")
# os.chdir("..")
print( os.rmdir("newdir"))