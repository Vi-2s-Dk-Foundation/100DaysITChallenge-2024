# OOP advanced topics
# Inheritance
# Polymorphism
# Encapsulation
# Abstraction

class Vehicle:
    def __init(self, brand, model, vin):
        self.brand = brand
        self.model = model
        self.__vin = vin # Private attribute
    
    # Use a get method for private attribute access outside class
    def get_vin(self):
        return self.__vin

    # Move method for vehicle
    def move(self):
        print(f"{self.brand {self.model} ({self.__vin}) is moving}")

class Car(Vehicle): # Inherits everything from Vehicle
    def __init__(self, brand, model, color, vin):
        super().__init__(brand, model, vin)
        self.color = color

    def move(self):
        print(f"{self.brand {self.model} ({self.__vin}) is moving ON LAND!}")

class Boat(Vehicle): # Inherits everything from Vehicle
    def move(self):
        print(f"{self.brand {self.model} ({self.__vin}) is moving ON WATER!}")

# Create instances to show polymorphism in action
my_car = Car("Toyota", "Camry", "Blue", "12345")
my_boat = Boat("Yamaha", "WaveRunner", "09876")

my_fleet_vehicles = [my_car, my_boat]   # List of objects

# Loop through all my vehicles to move together
for vehicle in my_fleet_vehicles:
    vehicle.move() # Different behaviors for different objects

# Due to encapsulation, we cannot access VIN directly, 
# but brand, model and color are ok

print(my_car.brand) # Brand is public
# print(my_car.__vin) # ERROR!!!

# instead
print(my_car.get_vin()) # Accessed private attribute through publis method
