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
    self.owner = input("Enter your name: ")

    # Schedule parking
    def sch_parking(self):

    self.owner = input("Enter your name: ")
        self.make = input("Enter your vehicle make: ")
        self.model = input("Enter your vehicle model: ")
        self.model_year = input("Enter your vehicle model year: ")
        self.car_type = input("Enter your vehicle weight: ")
        print(f"Name: ")
        print(f"Vehicle make: {self.make}.")
        print(f"Vehicle model: {self.model}.")
        print(f"Vehicle model year: {self.model_year}.")
        print(f"Vehicle weight: {self.car_type}.")
        confirm = input("Is this information correct? Type 'Yes' or 'No'.")

        if confirm == "Yes":
            print("You may enter the automatic parking garage.")
        elif confirm == "No":
            print("You may re-enter the information.")
        else:
            print("You must respond either 'Yes' or 'No'.")

    def end_parking(self):
        input("Enter your name")
        # User can claim their vehicle

print("Enter info: ")
car = Vehicle()

# User prompt to enter their name
print("Enter your name: ")
owner_name = input()
print(f"Hello, {owner_name}. Welcome to the Pythonville Automatic Parking Garage.")

# User prompt to enter vehicle make, model, model year, weight
print("Enter vehicle make: ")
make = input()

print("Enter vehicle model: ")
model = input()

print("Enter vehicle model year: ")
model_year = input()

print("Enter vehicle weight: ")
weight = input()
