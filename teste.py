import os

os.system('cls')

#declaração

a = 6
b = 4
c = 7


#processamento
soma = a + b + c
menos = a - b - c
multiplicação = a * b * c
divisão = a / b / c
expresão_matematica = a / b + c

#saída
print('-'*70)
print(f'o resultado da multiplicação é : {multiplicação} ')
print(f'o resultado da soma é: {soma}')
print(f'o resultado da divisão: {divisão}')
print(f'o resultado da expresão numerica é : {expresão_matematica}')
print(f'o resultado do menos é: {menos}')
print(f'-------------------------------------')

#questionario

nome = str(input('coloque um nome aqui: '))
nascimento = str(input('coloque sua data de nascimento: '))
município = str(input('coloque o nome de sua cidade:  '))
comida = str(input('coloque o nome da sua comida favorita: '))

#saída 
print('-'*70)
print(f'Meu nome é {nome}, nasci em {nascimento}; na cidade de {município} e minha comida favorita é {comida}')
print('')


