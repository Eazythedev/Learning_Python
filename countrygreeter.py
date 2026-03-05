#
# countrygreeter.py
# Country Greeter
#
# Created by Ezaiah Akyeem
# Date Created: March 5, 2026
# A program that greets you in multiple languages depending on which you select.

print("Welcome to the country selector!")
print("Select between the following countries and you will be greeted in that language.")
print("Select your country by entering a number.")
print("Type:\n1. U.S.A. / U.K. / Canada / Australia / New Zealand\n2. México / España / Brasil"
      "\n3. La France\n4. Italia\n5. Sverige\n6. Yaad(Jamaica)\n7. Lietuva(Lithuania)\n8. Norge")

country = int(input())

if country == 1:
    print("Good morning!")
elif country == 2:
    print("¡Buenos días!")
elif country == 3:
    print("Bonjour!")
elif country == 4:
    print("Buongiorno!")
elif country == 5:
    print("god morgon!")
elif country == 6:
    print("Maanin!")
elif country == 7:
    print("Labas rytas!")
elif country == 8:
    print("God morgen!")
else:
    print("Good morning!")
