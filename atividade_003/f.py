#Faça um programa onde o usuário tenta adivinhar o número que o computador 
#está ‘pensando’.


import os 
import random

#entrada 

print('adivinhe o número que a maquina está pensando!')
numero_aleatorio = random.randint(1,6)
usuario = float(input('entre com um número aleatorio de 1,6: '))

print(f'o computador selecionou {numero_aleatorio: .2f}')

