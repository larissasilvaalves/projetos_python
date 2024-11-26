#Faça um programa que leia um número indeterminado de notas (pressione ‘s’ ou ‘0’ para sair). 
#Após esta entrada de dados, faça o seguinte:
#• Mostre a quantidade de notas que foram lidas.
#• Exiba todas as notas na ordem em que foram informadas.
#• Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo da outra.
#• Calcule e mostre a soma das notas.
#• Calcule e mostre a média das notas.

import os 
import random

os.system('cls')
notas = []
soma = 0
quantidade = 0

nota = int(input('Digite suas notas: '))

while nota != "s" and nota != "0":
  
    soma += int(nota)
    notas.append(nota)
    nota = input('digite suas notas: ')

print(f'nota {notas}')

quantidade = len(notas)
print(quantidade)

media = soma/quantidade
print(media)

inverso = notas[::-1]
print(inverso)

for c in range(0, quantidade):
    print(notas[c])

print('fim do programa.')