import os 

os.system('cls')

print('-'*70)
print('operadores úteis para')
print('strings e estuturas de dados')
print('='*70)

texto = "olá, mundo"

print(f'texto: {texto}')
if 'Mundo' in texto: 
    print('A palavra "mundo" está presente na string.')
else: 
    print('A palavra "mundo" não está presente na string.')

print('.'*70)

texto2 = 'ola, python!'

print(f'Texto: {texto2}')
if "mundo" not in texto2:
    print('A palavra "mundo" não está presente na string.')
else:
    print('A palavra "mundo" está presente na string.')
print('-'*70)