import os 

os.system('cls')

#dicionario
 
cores = {}


for i in range(5):
    chave = input(f'Adicione uma cor {i + 1}: ')
    valor = input(f'Adcione uma descrição sobre a cor {chave}: ')
    cores[chave] = valor

print('Iniciando o programa.')
print('---------------------------------')
print('')


print(f'Sua lista irá ficar: {cores}')
print('')

while True:
    print('-'*70)
    print('/n Menu de opcões')
    print('1. Trocar descrição de cor.')
    print('2. Adicionar mais uma cor.')
    print('3. Modificar cor. ')
    print('4. Ordem alfabetica.')
    print('5. Relatorio do dicionário.')
    print('6. sair.')
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

    if opcao == '4':
        print(f'Sua lista em ordem alfabetica:')
        for cor, descricao in sorted(cores.items()):
            print(f'{cor}: {descricao}')

    if opcao == '5':
        primeira_letras = [cor[0].lower() for cor in cores]
        print(f'As primeiras letras iram ser "{primeira_letras}"')
        print(len(primeira_letras))


    if opcao == '6':
        print('sair do programa!')
        break