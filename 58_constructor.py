"""


"""

# self will be passed automatically in given example we provide 4 values to constructor.
class a1:

    # default constructor

    # def __init__(self):
    #
    #     print("hello, I am person.")
    #
    # parameterised constructor
    def __init__(self,n,o,w):
        self.name=n
        self.occuupation=o
        self.networth=w
        print("hello, I am person.")


    def info(self):
        print(f"{self.name} is an {self.occuupation}.")




a= a1("darsh","rikama",00)
b=a1("vedant","none",90)


print(a.name, a.occuupation, a.networth, sep="     ", end="\n ")

a.name = "abhi"
a.occuupation = "tester"
a.networth = 25
a.info()
b.info()
#
# b.ab(3)
