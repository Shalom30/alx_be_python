FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return (celsius + 32) * CELSIUS_TO_FAHRENHEIT_FACTOR


try:
    temperature = float(input("Enter the temperature to convert: "))

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    if unit == "C":
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted}°F")
    elif unit == "F":
        converted = convert_to_celsius(temperature)
        print(f"{temperature} F is {converted} C")
except ValueError:
    print("Invalid input. Please enter a float value")
