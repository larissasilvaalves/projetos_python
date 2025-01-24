#Crie uma função que receba uma lista de números. Depois retorne duas listas com os números pares,
#os números ímpares, a quantidade de números pares e a quantidade de números ímpares.
import os 

os. system('cls')

def numeros(lista):
    
    numeros_pares = []
    numeros_impares = []

    for nume in lista:
        
        nume = int(nume)

        if nume % 2 == 0 :
            numeros_pares.append(nume)
        else:
            numeros_impares.append(nume) 

        quantidade_par = len(numeros_pares)
        quantidade_impar = len(numeros_impares)

    return numeros_impares, numeros_pares, quantidade_par, quantidade_impar
    

lista = [ '1', '2', '3', '4', '5']
impares, pares, quantidade_par, quantidade_impar = numeros(lista)
print(f'impares: {impares}')
print(f'pares: {pares}')
print(f'Tem {quantidade_impar} números impares.')
print(f'Tem {quantidade_par} números pares')