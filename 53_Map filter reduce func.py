"""

 Map, Filter and Reduce

In Python, the map, filter, and reduce functions are built-in functions that allow you to apply a function to a sequence of elements and return a new
sequence. These functions are known as higher-order functions, as they take other functions as arguments.

------------map-----------

The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements.
The map function has the following syntax:

map(function, iterable)

The function argument is a function that is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other
iterable object.


---------------filter------------------

The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns a new sequence
containing only the elements that meet the predicate.
syntax:
filter(predicate, iterable)

The predicate argument is a function that returns a boolean value and is applied to each element in the iterable argument.
The iterable argument can be a list, tuple, or any other iterable object.



--------------reduce----------------------

The reduce function is a higher-order function that applies a function to a sequence and returns a single value. It is a part of the functools module in
 Python and has the following syntax:

reduce(function, iterable)

1) The function argument is a function that takes in two arguments and returns a single value. The iterable argument is a sequence of elements,
 such as a list or tuple.
2) The reduce function applies the function to the first two elements in the iterable and then applies the function to the result and the next element,
and so on. The reduce function returns the final result.



 -------------------------lambda function used in reduce ------------------------------
The reduce function applies the function to the first two elements in the iterable and then applies the function to the result and the next element,
and so on. The reduce function returns the final result.

*****Here is an example of how to use the reduce function:

from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]
# Calculate the sum of the numbers using the reduce function sum = reduce(lambda x, y: x + y, numbers)
# Print the sum
print(sum)

I) In the above example, the reduce function applies the lambda function lambda x, y: x + y to the elements in the numbers list. The lambda function adds the
 two arguments x and y and returns the result. The reduce function applies the lambda function to the first two elements in the list (1 and 2), then
 applies the function to the result (3) and the next element (3), and so on. The final result is the sum of all the elements in the list, which is 15.
II) It is important to note that the reduce function requires the functools module to be imported in order to use it.
"""

def cube(x):
    return  x*x*x

l=[1,2,2,3,4,5,6,7,8]


"""MAP"""
# newl=[]
# for item in l:
#     newl.append(cube(item))
# print(newl)

# without using this lengty process we will use map function to do this work
# syntax of map---> variable = data_type(func_name,list or maping data name))
newl=list(map(cube,l))
print(newl)
# or
newl=list(map(lambda x:x*x*x,l))
print(newl)

"""FILTER"""
def filter_func(a):
    return a>4
newl =list(filter(filter_func,l))
print(newl)
# or
# newl =list(filter(lambda ,l))
# print(newl)



"""REDUCE--> higher order function but it will be import"""
from functools import reduce
sum= reduce(lambda s,y:s+y,l)
print(sum)