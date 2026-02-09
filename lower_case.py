# A decorator with arguments that prints the output in either upper case or lower case.
# Created by Ezaiah Akyeem / Eazythedev / Eruine
# Date: February 8, 2026

def change_case(n):
    def change_case(func):
        def myinner():
            if n == 1:
                a = func().lower()
            else:
                a = func().upper()
            return a
        return myinner
    return change_case

@change_case(1)
def the_function():
    return "This will be lower case."
