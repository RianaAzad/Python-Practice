def double(x):
    return x*2

num = [1,2,3,4]

double_num = list(map(double, num))

#print(double_num)


# ------- Make a list of string numbers into list of int numbers --------
str_list = ['1', '2', '3', '4']
int_list = list(map(lambda x: int(x), str_list))
print(int_list)


# Add list of numbers using map 
num1 = [1,2,3]
num2 = [3,2,1]
num3 = [1,2,3]

sum = list(map(lambda x,y,z: x+y+z, num1, num2, num3))
print(sum)

names = ['Mitu', 'Ritu', 'Vitu']
ages = [15, 18, 17]

details = dict(map(lambda x,y: ("Name: "+x, "Age: " + str(y)), names, ages))
print(details)


# Python 3
my_pets = ['alfred', 'tabitha', 'william', 'arla']

uppered_pets = list(map(str.upper, my_pets))

print(uppered_pets)

'''
Syntax: map(func, *iterables)
Where func is the function on which each element in iterables (as many as they are) would be applied on. Notice the asterisk(*) on iterables? It means there can be as many iterables as possible, in so far func has that exact number as required input arguments. Before we move on to an example, it's important that you note the following:

In Python 2, the map() function returns a list. In Python 3, however, the function returns a map object which is a generator object. To get the result as a list, the built-in list() function can be called on the map object. i.e. list(map(func, *iterables))
The number of arguments to func must be the number of iterables listed.
'''
