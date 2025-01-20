#Questão B - Apostila python
import os 

os.system('cls')

#dicionario
 
cores = {} #criação do dicionário


for i in range(5):
    chave = input(f'Introduza a cor {i + 1}: ') 
    valor = input(f'Adicione uma descrição a cor {chave}: ')
    cores[chave] = valor

print('Iniciando o programa.')
print('---------------------------------')
print('')
print(f'Sua lista irá ficar: {cores}')
print('')

while True:
    print('-'*70)
    print('/n Menu de opcões')
    print('1. Adicionar mais uma cor.')
    print('2. Modificar cor. ')
    print('3. Ordem alfabetica.')
    print('4. Relatório do dicionário.')
    print('5. sair.')
    print()

    opcao = input('Escolha uma das opções (1 - 5): ')

    if opcao == '1':
        nova_chave = input('Adicone uma nova cor: ')
        novo_valor = input('Adicione o valor de sua cor:')
        cores.setdefault(nova_chave, novo_valor)
       
    print(f'Dicionário atualizado: {cores}')

    if opcao == '2':
     
        for indice, (cor, descricao) in enumerate(cores.items()):
            print(f'{indice}. {cor}: {descricao}')
     
        indice_escolhido = int(input('Escolha o número da cor que deseja mudar (índice): '))
        cor_escolhida = list(cores.keys())[indice_escolhido]
        descricao_atual = cores[cor_escolhida]

        print(f'Você escolheu mudar a cor {cor_escolhida} com a descrição: "{descricao_atual}"')

        nova_descricao = input(f'Digite a nova descrição para {cor_escolhida}: ')
        cores[cor_escolhida] = nova_descricao
 
        print('\nDicionário atualizado:')
        for cor, descricao in cores.items():
            print(f'{cor}: {descricao}')
    
    if opcao == '3':
        print(f'Sua lista em ordem alfabetica:')   
        for cor, descricao in sorted(cores.items()):
            print(f'{cor}: {descricao}')

    if opcao == '4':
        primeira_letras = [cor[0].lower() for cor in cores]
        print(f'As primeiras letras iram ser "{primeira_letras}"')
        print(len(primeira_letras))

    if opcao == '5':
        print('saindo do programa!')
        break