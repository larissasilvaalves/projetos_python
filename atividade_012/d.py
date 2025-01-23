
import os 

os.system('cls')

def fahrenheit_para_celsius(fahrenheit):
   
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
celsius = fahrenheit_para_celsius(fahrenheit)
print(f"A temperatura de {fahrenheit}°F é equivalente a {celsius:.2f}°C.")

