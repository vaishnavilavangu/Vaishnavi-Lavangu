#function to convert celsius to fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
#function to convert celsius to kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15
#function to convert fahrenheit to celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
#function to convert fahrenheit to kelvin
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15
#function to convert kelvin to celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15
#function to convert kelvin to fahrenheit
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Main program
#prints the statements
print("Temperature Conversion Tool")
print("1. Celsius to Fahrenheit")
print("2. Celsius to Kelvin")
print("3. Fahrenheit to Celsius")
print("4. Fahrenheit to Kelvin")
print("5. Kelvin to Celsius")
print("6. Kelvin to Fahrenheit")

ch = int(input("Choose a conversion (1 to 6): "))
temp = float(input("Enter the temperature to convert: "))

if ch== 1:
    result = celsius_to_fahrenheit(temp)
    print(f"{temp}°C is equal to {result:.2f}°F")
elif ch == 2:
    result = celsius_to_kelvin(temp)
    print(f"{temp}°C is equal to {result:.2f}K")
elif ch == 3:
    result = fahrenheit_to_celsius(temp)
    print(f"{temp}°F is equal to {result:.2f}°C")
elif ch == 4:
    result = fahrenheit_to_kelvin(temp)
    print(f"{temp}°F is equal to {result:.2f}K")
elif ch == 5:
    result = kelvin_to_celsius(temp)
    print(f"{temp}K is equal to {result:.2f}°C")
elif ch == 6:
    result = kelvin_to_fahrenheit(temp)
    print(f"{temp}K is equal to {result:.2f}°F")
else:
    print("Invalid choice. Please select a valid option.")
