import os 

os.system ('cls')

#entrada
nome = str(input('entre com o seu nome completo: '))

#processamento
nome_quebrado = nome.split()
prmeiro_nome = nome_quebrado[0]
ultimo_nome = nome_quebrado[-1]

#saída
print(f'{nome}')
print(f'{nome_quebrado}')
print(f'o primeiro nome é: {prmeiro_nome}')
print(f'o ultimo nome é: {ultimo_nome}')