# Simple class

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        # simply print
        print(f"Woof! I'm {self.name} the {self.breed}" )

# Create an object from class
my_dog = Dog("Bingo", "German Shepherd")
my_dog.bark()

#Another class

class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def start_car(self):
        print(f"Starting the {self.color} {self.model}")

    def stop_car(self):
        print(f"Stopping the {self.color} {self.model}")

my_car = Car("Black", "Jaguar")
my_car.start_car()
my_car.stop_car()
