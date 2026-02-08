# A function that holds a dictionary with information for a car unpacked with **
# Created by Ezaiah Akyeem / Eazythedev / Eruine
# Date: February 6, 2026

def the_function_2(make, model):
    print("This car is a", make, model)

vehicle = {"make": "Mitsubishi", "model": "Lancer"}
the_function_2(**vehicle)
