# Base class
class Mover:
    def move(self):
        pass

# Vehicle classes
class Car(Mover):
    def move(self):
        print("Driving ")

class Plane(Mover):
    def move(self):
        print("Flying ")

class Boat(Mover):
    def move(self):
        print("Sailing ")

# Animal classes
class Dog(Mover):
    def move(self):
        print("Running ")

class Bird(Mover):
    def move(self):
        print("Flying ")

class Fish(Mover):
    def move(self):
        print("Swimming ")

# Test them
def perform_moves(movers):
    for mover in movers:
        mover.move()

# List of various movers
movers_list = [Car(), Plane(), Boat(), Dog(), Bird(), Fish()]
perform_moves(movers_list)
