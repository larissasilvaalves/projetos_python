import os 

os.system('cls')

print('-'*70)
print('QUANTAS VOGAIS TEM EM SUA FRASE!')

frase = str(input('entre com sua frase: ' ))

quantidade_de_A = frase.count('a')
quantidade_de_E = frase.count('e')
quantidade_de_I = frase.count('i')
quantidade_de_O = frase.count('o')
quantidade_de_U = frase.count('u')

print(f'A quantidade de a quantidade de A que aparece foi {quantidade_de_A}')
print(f'A quantidade de a quantidade de E que aparece foi {quantidade_de_E}')
print(f'A quantidade de a quantidade de I que aparece foi {quantidade_de_I}')
print(f'A quantidade de a quantidade de O que aparece foi {quantidade_de_O}')
print(f'A quantidade de a quantidade de U que aparece foi {quantidade_de_U}')
print('-'*70)