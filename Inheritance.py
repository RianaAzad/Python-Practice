class Vehicle:
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year

    def startEngine(self):
        return "Engine Started."
    def stopEngine(self):
        return "Engine Stopped"
    def getInfo(self):
        return f"{self.year} {self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, year, no_of_doors) -> None:
        super().__init__(make, model, year)
        self.no_of_doors = no_of_doors

    def openTrunk(self):
        return "Trunk Opened"
    
    def getInfo(self):
        base_info = super().getInfo()
        return f"{base_info} {self.no_of_doors} doors"
    
class Bicycle(Vehicle):
    def __init__(self, make, model, year, type_of_bike):
        super().__init__(make, model, year)
        self.type_of_bike = type_of_bike

    def ring_bell(self):
        return "Bell rung"

    def get_info(self):
        base_info_2 = super().get_info()
        return f"{base_info_2}, {self.type_of_bike} bike"


# Example usage of Bicycle class
bicycle = Bicycle("Giant", "Escape 3", 2022, "road")
print(bicycle.getInfo())  
print(bicycle.ring_bell()) 
    
car = Car('Toyota', "Camry", 2021, 4)
print(car.getInfo())
print(car.startEngine())
print(car.openTrunk())
print(car.stopEngine())