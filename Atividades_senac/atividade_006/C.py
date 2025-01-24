#Faça um programa que procure na lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] e produza:
#• O intervalo de 1 até 9
#• O intervalo de 8 até 13
#• Os números pares
#• Os números ímpares
#• Os múltiplos de 2, 3 e 4
#• Lista reversa
#• O produto dos intervalos 5-6 por 11-12

import os 

os.system('cls')

print('-'*70)
print('ATIVIDADE C')
print('='*70)

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(lista_numeros)


#fatiamento
print('-'*70)
print('fatiamento')
print('='*70)

lista2 = lista_numeros[0:9]
print(f'intervalo em {lista2} ')

lista3 = lista_numeros[7:13]
print(f'intervalo em {lista3}')
 
print()

#numeros pares da lista
print('NÚMEROS PARES E ÍMPARES')

for c in range(0, 15):
    if c % 2 == 0:
        print(f'pares {c}')
    else:
        continue 
for c in range(0,15):
    if c % 2 != 0:
        print(f'impares {c}')

print()
print('LISTA REVERSA')

#lista reversa

lista_reversa = lista_numeros[15::-1]
print(f'A lista reversa fica {lista_reversa}')

print()

# MULTIPLOS DE 2,3,4
print('MULTIPLOS E 2,3,4')

for c in range (0,15):
    if c %2 == 0:
        print(f'os multiplos de 2 são {c}')

    else:
        continue
    

   
    if c %3 == 0:
        print(f'os multiplos de 3 são {c}')
        print('-'*70)    
        
    if c %4 == 0:
        print(f'os multiplos de 4 são {4}')
        print('-'*70)

print()
#produtos de 5-6 e 11-12
print('OS PRODUTOS DE 5-6 POR 11-12')
print('-----------------------')
conta1 = 5 * 11
conta2 = 6 * 12
print('----------------------------------')
print(f'Os resultdos serão {conta1} e {conta2}')
