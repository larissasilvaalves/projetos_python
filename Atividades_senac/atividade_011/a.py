import os

os. system('cls')

#meu dicionario

dici = {}

print(dici)


# menu para o usuário

while True:
    print('-'*70)
    print('\n Menu principal: ')
    print('1. Adiconar um par chave-valor: ')
    print('2.mostrar itens do dicionario: ')
    print('3. sair do programa.')


    opcao = input(' Escolha entre as (1 - 3): ')

    if opcao == "1":

        chave = input ('Digite a chave: ')
        valor = input ('digite o valor da chave: ')
        dici[chave] = valor
        print(f'par {chave}: {valor} adicionado')

    elif opcao == '2':

        if dici:
            print('itens adicionados no dicioário:', dici.items())
        else:
            print('O Dicionario está vazio. adicione alguem item')

    if opcao == '3': 

        print('saindo do programa.')
        break
    

    
    