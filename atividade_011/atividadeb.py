import os 

os.system('cls')

#dicionario
 
cores = {} #criação do dicionário

#o for é um tipo de programação que mexe com a sequência, com ele eu posso pedir para que o programa
#repita o código quantas vezes necessaria.
for i in range(2):
    chave = input(f'Introduza a cor {i + 1}: ') 
    valor = input(f'Adicione uma descrição a cor {chave}: ')
    cores[chave] = valor

#Utilizando o 'for', eu fiz que o programa repetisse a pergunta 5 vezes, após o usuario responder
#Eu introduzia as duas strings(chave-valor) dentro do dicionário; 

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
        print('\nDicionario atualizado:')

    print(f'Dicionário atualizado: {cores}')
#
#
#
#
#
#

    if opcao == '2':
        # Exibindo as cores e suas descrições
        for indice, (cor, descricao) in enumerate(cores.items()):
            print(f'{indice}. {cor}: {descricao}')
        # Perguntando ao usuário qual cor ele deseja alterar
        indice_escolhido = int(input('Escolha o número da cor que deseja mudar (índice): '))
        # Obtendo a cor e descrição correspondente ao índice
        cor_escolhida = list(cores.keys())[indice_escolhido]
        descricao_atual = cores[cor_escolhida]
        print(f'Você escolheu mudar a cor {cor_escolhida} com a descrição: "{descricao_atual}"')
        # Perguntando pela nova descrição
        nova_descricao = input(f'Digite a nova descrição para {cor_escolhida}: ')
        # Atualizando a descrição no dicionário
        cores[cor_escolhida] = nova_descricao
        # Exibindo o dicionário atualizado
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