#Desenvolva um programa que solicite três valores ao usuário. Em seguida, calcule e exiba a soma e a multiplicação desses valores.
import os 

os.system('cls')

def somas(a , b, c):

    s = a + b + c
    return s


def multiplicacoes(a, b, c):

    m = a * b * c
    return m


a = int(input('Primeiro digito: '))
b = int(input('Srgundo digito: '))
c = int(input('Terceiro digito: '))
multiplicacao = multiplicacoes(a, b , c)
soma = somas(a, b, c)
# a = int(input('Primeiro digito: '))
# b = int(input('Srgundo digito: '))
# c = int(input('Terceiro digito: '))
print('Fazendo as contas')
print(f'A soma dos três digitos é : {soma}')
print(f'A multiplicação dos três digitos é igual á : {multiplicacao}')

    