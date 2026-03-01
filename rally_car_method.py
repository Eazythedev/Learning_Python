# Car Model Year Check
# Created by Ezaiah Akyeem / Eazythedev / Erujine
# Date Created: February 28, 2026

class Rally_Car(Car):
    def __init__(self, make, model, myear):
        super().__init__(make, model)
        self.model_year = myear

    def Car_Info_Expl(self):
        print(f"This rally car is a {self.model_year} {self.make} {self.model}. It is all-wheel drive and is built for rally racing.")

c2 = Rally_Car("Mitsubishi", "Lancer", 1993)
c2.Car_Info_Expl()
