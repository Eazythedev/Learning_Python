#
# countrygreeterv2.py
# Country Greeter V2
#
# Created by Ezaiah Akyeem
# Date Created: March 5, 2026
# A program that greets you in multiple languages depending on which you select.

print("Welcome.")
print("Select a country from the following list and you will be greeted in that language.")
print("Type the name of the country.")
print("\n - United States\n - United Kingdom\n - Ireland \n - Canada\n - Australia\n - New Zealand\n - México (Mexico)\n"
      " - España (Spain)\n - Brasil (Brazil)\n - La France (France)\n - Italia (Italy)\n - Sverige (Sweden)\n"
      " - Yaad (Jamaica)\n - Lietuva (Lithuania)\n - Norge (Norway)")

country = input()

if country == ("United States" or country == "USA" or country == "US" or country == "U.S." or country == "U.S.A."
        or country == "United Kingdom" or country == "U.K." or country == "Great Britain" or country == "Scotland"
        or country == "Wales" or country == "Northern Ireland" or country == "Ireland" or country == "Canada"
        or country == "Australia" or country == "New Zealand"):
    print("Hello, how are you?")
elif country == "Mexico" or country == "Spain" or country == "Brazil":
    print("¿Hola, cómo estás?")
elif country == "La France" or country == "France":
    print("Bonjour comment allez-vous?")
elif country == "Italia" or country == "Italy":
    print("Ciao, come stai?")
elif country == "Sverige" or country == "Sweden":
    print("Hallå, hur mår du?")
elif country == "Yaad" or country == "Jamaica":
    print("Ello ow yuh duh?")
elif country == "Lietuva" or country == "Lithuania":
    print("Sveiki, kaip laikaisi?")
elif country == "Norge" or country == "Norway":
    print("Hallo, hvordan har du det?")
else:
    print("Hello, how are you?")
