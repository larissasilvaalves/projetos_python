#Crie uma função que receba uma temperatura em fahrenheit e retorne o valor em graus célsius.
import os 

os.system('cls')

def fahrenheit_para_celsius(fahrenheit):
    # Converte a temperatura de Fahrenheit para Celsius
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# Solicita a temperatura em Fahrenheit do usuário
fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

# Converte para Celsius e exibe o resultado
celsius = fahrenheit_para_celsius(fahrenheit)
print(f"A temperatura de {fahrenheit}°F é equivalente a {celsius:.2f}°C.")



refazer o codigo em casa
