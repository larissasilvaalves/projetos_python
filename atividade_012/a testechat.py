#Crie uma função que receba uma lista de números. Depois retorne duas listas com os números pares,
#os números ímpares, a quantidade de números pares e a quantidade de números ímpares.
import os 

os. system('cls')

def numeros(lista):
    numeros_pares = []
    numeros_impares = []

    for nume in lista:
        # Converte nume para inteiro, se já não for
        # nume = int(nume)  # Garantir que nume é um número
        
        if nume % 2 == 0:
            numeros_pares.append(nume)
        else:
            numeros_impares.append(nume)

    return numeros_impares, numeros_pares

# Exemplo de lista com strings numéricas
lista = [1,2,3,4,5,6,7,8,9]  # Lista de strings

impares, pares = numeros(lista)

print(f'Impares: {impares}')
print(f'Pares: {pares}')
