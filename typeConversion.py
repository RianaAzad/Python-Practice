'''
Type conversion in Python refers to converting one data type into another. This can be done either implicitly by Python or explicitly by the programmer.

---------- Implicit Type Conversion ---------
Implicit type conversion, also known as coercion, is automatically performed by Python when an operation involves two or more different data types. Python converts one type into another to avoid data loss.
'''
num_int = 123
num_float = 1.23
num_new = num_int + num_float

print("datatype of num_int:", type(num_int))
print("datatype of num_float:", type(num_float))

print("Value of num_new:", num_new)
print("datatype of num_new:", type(num_new))

#In the example above, num_int is an integer and num_float is a float. When we add them together, Python implicitly converts num_int to a float and then performs the addition, resulting in a float.


'''
----- Explicit Type Conversion ----------
Explicit type conversion requires the use of predefined functions to convert a value from one type to another. Common functions used for explicit type conversion include int(), float(), str(), list(), tuple(), and set().
'''

# -------- Convert to Integer ---------
num_str = "1234"
num_float = 123.45
num_int1 = int(num_str)
num_int2 = int(num_float)
print(num_int1)
print(num_int2)

# -------- Convert to Float ---------
num_str2 = "123.345"
num_float1 = float(num_str2)
num_float2 = float(num_int1)

# -------- Convert to String ---------
num_str3 = str(num_float)
num_str4 = str(num_int1)

# -------- Convert to List ---------
tuple_data = (1, 2, 3)
str_data = "Riana"

list1 = list(tuple_data)
list2 = list(str_data)
print(list1)
print(list2)

# -------- Convert to Tuple ---------
tuple1 = tuple(list1)
tuple2 = tuple(str_data)
print(tuple1)
print(tuple2)

# -------- Convert to Set ---------
set1 = set(list1)
set2 = set(str_data)

print(set1)
print(set2) # In Python, sets are unordered collections of unique elements. This means that the elements in a set do not have a specific order, and their arrangement can vary. When you convert a string to a set, the characters are added to the set in an arbitrary order determined by the underlying implementation.
'''
The order of elements in set2 is not guaranteed to be the same each time you run the program. The primary purpose of a set is to store unique elements, not to maintain a specific order. If you need to maintain the order of characters, you should use a different data structure, such as a list or an ordered collection.
'''

# For getting ordered list:
from collections import OrderedDict

str_data = "Riana"
ordered_set =  "".join(OrderedDict.fromkeys(str_data))
print(ordered_set)