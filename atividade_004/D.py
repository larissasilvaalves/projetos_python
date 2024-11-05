import os 

os.system('cls')

frase = 'Amo Meu Morceguin'


#processamento

quantidade_caracteres = len(frase)
print(f'A frase {frase} \ncontém {quantidade_caracteres} caracteres!')
print('-'*70)

minuscula = frase.lower()
print(f'a frase minúscula irá ficar "{minuscula}"')
print('-'*70)

maisculas = frase.upper()
print(f'a frase completamente maiúscula irá ficar "{maisculas}"')
print('-'*70)

separacao_variaveis = frase.split(" ")
print(f'{separacao_variaveis}')
