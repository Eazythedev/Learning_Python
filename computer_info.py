# A function that holds information using a **kwargs
# Created by Ezaiah Akyeem / Eazythedev / Eruine
# Date: February 6, 2026

def computer_info(**computer):
    print("The computer's make is " + computer["brand"])

computer_info(model = "8800", brand = "Altair")
