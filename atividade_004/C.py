import os 
os.system ('cls')

nome = str(input('coloque o seu nome inteiro aqui: '))

print(f'nome: {nome}')
if 'oliveira' in nome:
    print('A palavra "oliveira" está presente no nome')
else:
    print('A palavra "Oliveira" não está presente no nome')

print('.'*70)