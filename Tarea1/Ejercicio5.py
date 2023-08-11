# Crear una función que convierta grados Fahrenheit a grados Celsius.

def farhrenheit_to_celsius(farhrenheit):
    celsius= (farhrenheit -32)* 5/9
    return celsius

farhrenheit= float(input("Enter a number in ° celsius: "))
celsius= (farhrenheit_to_celsius(farhrenheit))
print(f"The conversion from {farhrenheit}°F to °C is: {celsius}°C ")

