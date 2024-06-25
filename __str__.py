class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}"
    
    def __repr__(self) -> str:
        return f"From repr, Name: {self.name}"

obj = Person('a', 23)
print(obj)
print(obj.__str__())
print(obj.__repr__())
print(str(obj))
print(repr(obj))

'''

**** These are known as dunder methods/ magic methods ******

__str__ vs __repr__
Both __str__ and __repr__ methods are used to provide a string representation of an object in Python, but they serve different purposes and are used in different contexts.

__str__
***Purpose: The __str__ method is meant to provide a "pretty" or human-readable string representation of an object. This is the string that you, as a user, would like to see.
***Use Case: When you print an object using print() or str(), Python calls the __str__ method.
***Example: Think of it as the way you would describe the object to someone who doesn't need to know all the technical details.
__repr__
***Purpose: The __repr__ method is meant to provide an "official" string representation of an object that could ideally be used to recreate the object. It's more for developers and debugging purposes.
***Use Case: When you use the repr() function or just type the object name in the interactive Python shell, Python calls the __repr__ method.
***Example: Think of it as the way you would describe the object to another programmer who might need to know exactly what the object is and how to recreate it.

-------Key Points:-------
+Human-readable (__str__): Aimed at users; shows a readable format.
+Unambiguous (__repr__): Aimed at developers; shows a detailed, often more precise, format that can be used to recreate the object.
--------When to Use Each------
Use __str__ when you want a nice, readable output of the object for end users.
Use __repr__ when you need a detailed, precise output that can help with debugging or recreating the object.


'''