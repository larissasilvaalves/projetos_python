#Faça um programa que solicite separadamente o nome, o nome do meio e o sobrenome de uma pessoa. Em seguida, imprima o nome completo.
import os 

os.system('cls')

def imprimir_nome ():

    print(f'Seu nome completo vai ser: {nome} {sobrenome} {ultimo_nome}')
    nome = input('Escreva seu primeiro nome: ')
    sobrenome = input('Seu sobrenome: ')
    ultimo_nome = input('Seu ultimo nome: ')
    
imprimir_nome()

