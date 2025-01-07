import os 

os.system('cls')

#dicionario
 
cores = {}


for i in range(5):
    chave = input(f'Adicione uma cor {i + 1}: ')
    valor = input(f'Adcione uma descrição sobre a cor {chave}: ')
    cores[chave] = valor

print('Iniciaciando o programa.')
print('---------------------------------')


print(f'Sua lista irá ficar: {cores}')

while True:
    print('-'*70)
    print('/n Menu de opcões')
    print('1. Trocar descrição de cor.')
    print('2. Adicionar mais uma cor.')
    print('3. Modificar cor. ')
    print('4. sair')
    print()

    
    opcao = input('Escolha uma das opções (1 - 4):')

    if opcao == '1':
    
        cor = input('Escolha escolha qual valor deseja trocar: ')

        nova_desc = input('Digite a nova descrição: ')

        if cor in cores:
            cores[cor] = nova_desc
            print(f'A cor {cor} foi encontrada e alterdada por: {nova_desc}')
        else:
            print('cor não foi encontrada.')

        print(f"lista alterada: {cores}")

    elif opcao == '2':

        nova_chave = input('Adicone uma nova cor: ')
        novo_valor = input('Adicione o valor de sua cor:')

        cores.setdefault(nova_chave, novo_valor)

    print(f'A nova lista ira ficar {cores}')

    if opcao == '3':

        chaves = input(f'Digite a cor que deseja mudar: ', (cores.keys()))

        for i in range(len(chaves)):
            chaves = chaves[i]
            if chave == chaves:
                cores[chave] = cores [chave]

        print(cores)