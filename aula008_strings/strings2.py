import os 


os.system('cls')

print('-'*70)
print('funções string')
print('='*70)

frase1= 'olá, Mundo!'
quantidade_caracteres = len(frase1)
print(f'A frase {frase1} \ncontém {quantidade_caracteres} caracteres')
print('-'*70)

minusculas = frase1.lower()
print(f'Frase original: {frase1}')
print(f'Frase nova: {minusculas}')
print('.'*70)

captalizada = frase1.capitalize()
print(f'Frase original: {frase1}')
print(f'Frase nova: {captalizada}')
print()

frase2 = '     olá, Mundo    '
sem_espaços = frase2.strip()
print(f'Frase original: {frase2}')
print(f'Frase nova: {sem_espaços}')
print()

substituicao = frase1.replace('mundo' , "python")
print(f'Frase original: {frase1}')
print(f'Frase nova: {substituicao}')
print()

lista = frase1.split(',')
print(f'Frase orginal: {frase1}')
print(f'Frase nova: {lista}')
print('.'*70)

lista = ['olá', 'mundo']
juncao = '-'.join(lista)
print(f'Frase orginal: {lista}')
print(f'Frase nova: {juncao}')
print('.'*70)