# Automatic Parking Garage System
# Created by Eazythedev / Erujine
# Date Created: March 2, 2026

class Vehicle:
    def __init__(self, make, model, model_year, car_type, owner):
        self.make = make
        self.model = model
        self.model_year = model_year
        self.car_type = car_type
        self.owner = owner

    # Park vehicle
    def park_vehicle(self):

    # Schedule parking
    def sch_parking(self):

print("Enter info: ")
car = Vehicle()

# User prompt to enter their name
print("Enter your name: ")
owner_name = input()
print(f"Hello, {owner_name}. Welcome to the Pythonville Automatic Parking Garage.")

# User prompt to enter vehicle make, model, model year, weight
print("Enter your vehicle make: ")
make = input()

print("Enter your vehicle model: ")
model = input()

print("Enter your vehicle model year: ")
model_year = input()

print("Enter your vehicle weight: ")
weight = input()
