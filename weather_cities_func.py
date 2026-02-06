# Function that prints the weather converted from fahrenheit to celsius in different cities

def fahrenheit_to_celsius(fahrenheit):
    return(fahrenheit - 32 ) * 5 / 9

print("Seattle temperature in celsius: ")
print(fahrenheit_to_celsius(77))
print("Cairo temperature in celsius: ")
print(fahrenheit_to_celsius(95))
print("Sapporo temperature in celsius: ")
print(fahrenheit_to_celsius(50))
