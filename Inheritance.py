class Parent: 
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def greet(self):
        return f"Hello, my name is {self.fname} {self.lname}."
    
class Child(Parent):
    pass


obj = Child("Riana", "Azad")
print(obj.greet())
