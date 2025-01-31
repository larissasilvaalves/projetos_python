#Desenvolva um programa que peça um número qualquer e calcule o dobro e o triplo desse número.
import os 

os.system ('cls')
#funções
def calculando(dobro, triplo):
    dobro = numero * 2
    triplo = numero * 3

    return dobro, triplo

#programa principal
numero = int(input('Escreva um número: '))

#invocando a função

resultado = calculando(dobro= numero, triplo=numero)
print(f'{resultado},  {resultado}')
