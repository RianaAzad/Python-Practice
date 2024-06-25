x = 10      # x is an integer object, which is immutable
x = x + 5   # This creates a new integer object and assigns it to x
print(x)    # Output: 15

s = "hello" # s is a string object, which is immutable
s = s + " world" # This creates a new string object and assigns it to s
print(s)    # Output: "hello world"


'''
Immutable Objects
Immutable objects are those whose state or value cannot be modified after they are created. If you need to change the value of an immutable object, you must create a new object with the new value.

Common examples of immutable objects in Python include:

Numbers: int, float, complex
Strings: str
Tuples: tuple
Frozen sets: frozenset
'''


# List example
l = [1, 2, 3]  # l is a list object, which is mutable
l.append(4)    # This modifies the original list object
print(l)       # Output: [1, 2, 3, 4]

# Dictionary example
d = {"a": 1, "b": 2}  # d is a dictionary object, which is mutable
d["c"] = 3            # This modifies the original dictionary object
print(d)              # Output: {'a': 1, 'b': 2, 'c': 3}


'''
Mutable Objects
Mutable objects are those whose state or value can be changed after they are created. Modifying a mutable object does not create a new object; it changes the original object.

Common examples of mutable objects in Python include:

Lists: list
Dictionaries: dict
Sets: set
User-defined classes: Any instance of a class you define, depending on the implementation.

'''


# *********************** 
'''
Key Differences
Modification:

Immutable: Cannot be changed after creation. Any modification results in a new object.
Mutable: Can be changed after creation. Modifications change the original object.
Identity:

Immutable: The object’s identity changes when it is "modified" because a new object is created.
Mutable: The object’s identity remains the same even when its content is modified.
'''