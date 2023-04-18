"""
#Getter setter in python.
for getter we use @ property decorator
for setter we use @ setter.getter_name decorator

*****Getter******

*****Setter******
"""

class example:
    def __init__(self,value):
        self._value = value
    def show(self):
        print(f"You Taken no is {self._value}")

    @property
    def getter(self):
        # print("you are in getter")
        return  10*self._value


    @getter.setter
    def setter(self,  new_value):
        # print("you are in setter")
        self._value= new_value/10


obj=example(12)
obj.setter=25  # set the value to the setter
print(obj.getter)
print(obj.setter)
obj.show()