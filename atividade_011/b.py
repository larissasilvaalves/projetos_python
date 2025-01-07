import os 

os.system('cls')

#dicionario
 
cores = {}


for i in range(5):
    chave = input(f'Adicione uma cor {i + 1}: ')
    valor = input(f'Adcione uma descrição sobre a cor {chave}: ')
    cores[chave] = valor

print(f'Sua lista irá ficar: {cores}')

while True:
    print('-'*70)
    print('/n Menu de opcões')
    print('1. Trocar cor do dicionario.')
    print('2. Adicionar mais uma cor.')
    print('3. Modificar cor  ')
    print('4. sair')

    
    opcao = input('Escolha uma das opções (1 - 4):')

    if opcao == '1':
    
        cor = input(' escolha a cor que deseja trocar: ')

        for chave in cores.items():
            print(chave)