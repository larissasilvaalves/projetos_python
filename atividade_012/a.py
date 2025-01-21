#Crie uma função que receba uma lista de números. Depois retorne duas listas com os números pares,
#os números ímpares, a quantidade de números pares e a quantidade de números ímpares.
import os 

os. system('cls')

lista = input('Adicione uma lista de números aqui:  ')

def numeros(lista):
    
    numeros_pares = []
    numeros_impares = []

    for nume in lista:
        if nume % 2 == 0 :
            numeros_pares.append(nume)
        else:
            numeros_impares.append(nume) 

    return numeros_impares, numeros_pares
    

print(f'{numeros_impares}')

        

