import os 

os.system('cls')


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + b: {s}')
    print(s)


a = int(input('Primeiro digito: '))
b = int(input('Segundo número:'))
soma(a , b)