# Film List
# Created by Eazythedev / Erujine
# Date Created: February 27, 2026

# Code causes error as is
class Film_List:
    def __init__(self, title, director, year, star_1, star_2, release_date, budget):
        self.title = title
        self.director = director
        self.year = year
        self.star_1 = star_1
        self.star_2 = star_2
        self.release_date = release_date
        self.budget = budget
        self.films = []

    def display_film_info(self):
        print(f"Film information: \n\n Title: {self.title} \n Director: {self.director} \n Year: {self.year} "
              f" \n Starring: {self.star_1} and {self.star_2} \n Release Date: {self.release_date} \n Budget: {self.budget}.")

    def add_film(self, film):
        self.films.append(film)
        film.input("Enter film title: ")

        print(f"\n Added: {film}")

the_film = Film_List()
film1 = Film_List("Rush Hour", "Brett Ratner", "1998", "Jackie Chan", "Chris Tucker", "September 18, 1998", "35 million USD")

# film1.display_film_info()
the_film.add_film()
print("\n What film what you like to add? Enter title: ")
