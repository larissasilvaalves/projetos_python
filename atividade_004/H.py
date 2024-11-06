#Faça um programa que leia o nome de um aluno e mostre quantas 
# vezes a letra 'o' aparece e em que posição ela aparece pela 
# primeira e última vez.


import os 

os.system('cls')

print('-'*70)
print('PROGRAMA DE LEITURA')
print()

#entrada
nome = str(input('Entre com o nome completo:'))

#processamento 

contagem = nome.count('o')
print(f'o nome completo tem {contagem} O.')

primeira_posicao = nome.find('o')
print(f'o primero O está na {primeira_posicao +1}° posição.')

ultima_posicao = nome.rfind('o')
print(f'o ultimo O está na {ultima_posicao}° posição.')

print()
