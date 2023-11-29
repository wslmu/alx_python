def convert_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

fahrenheit_temperature = 98.6
celsius_temperature = convert_to_celsius(fahrenheit_temperature)
print(f"{fahrenheit_temperature} Fahrenheit is {celsius_temperature:.2f} Celsius")
