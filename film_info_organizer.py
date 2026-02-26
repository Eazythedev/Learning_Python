# Film Information Organizer
# Created by Ezaiah Akyeem / Eazythedev / Erujine
# Date Created: 2-26-26

# Film Information Organization System that uses a class, an __init__() method, and another method.

class Film:
    def __init__(self, title, director, year, star_1, star_2, release_date, budget):
        self.title = title
        self.director = director
        self.year = year
        self.star_1 = star_1
        self.star_2 = star_2
        self.release_date = release_date
        self.budget = budget

    def Display_Film_Info(self):
        print(f"Film information: \n Title: {self.title} \n Director: {self.director} \n Year: {self.year} "
              f" \n Starring: {self.star_1} and {self.star_2} \n Release Date: {self.release_date} \n Budget: {self.budget}.")

film1 = Film("Rush Hour", "Brett Ratner", "1998", "Jackie Chan", "Chris Tucker", "September 18, 1998", "35 million USD")
film1.Display_Film_Info()
