# Match case Statements  --> it is similar as switch case

# import os #used for detecting version of python.
# os.system("python --version")


x=int(input("Enter value of x : "))
match x:
    case 0:
        print("X is zero.")
    case 4:
        print("X is four.")
    case 8:
        print("X is eight.")
    case _ if x!=70:
        print(x," is not equal to 70.")
    case _ if x!=80:
        print(x," is not equal to 80.")
    case _ if x!=90:
        print(x," is not equal to 90")
    case _:
        print(x)
