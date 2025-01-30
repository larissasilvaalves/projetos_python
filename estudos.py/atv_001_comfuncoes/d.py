#Faça um programa que receba um número inteiro e exiba seu sucessor e antecessor.
import os 

os.system('cls')

#funções
def ordens_relativas(antecessor, sucessor):
    antecessor = nume1 - 1 , nume2 + 1
    sucessor = nume1 - 1, nume2 + 1

    return antecessor, sucessor
    
#programa principal
nume1 = int(input('adicione o seu número: '))
nume2 = int(input('adicione seu segundo número: '))

#invocação da função

resultado = ordens_relativas(nume1, nume2)

print(resultado)
