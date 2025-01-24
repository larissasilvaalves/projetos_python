#Crie um programa que peça ao usuário 2 números maiores que 0 e menores que 11. 
# Depois mostre um menu com as seguintes operações:
#1. Soma: 2. Subtração : 3. Produto : 4. Divisão : 5. Divisão inteira : 6. 
# Resto da divisão.
#O usuário deverá escolher um número maior ou  igual a 1 e menor ou igual a 6. 
#Em seguida, você criará funções que retornem os resultados das operações, imprimindo os resultados na tela.

import os 

os.system('cls')

def numeros():

    nume1 = float(input('Adicione um número maior que zero: '))
    nume2 = float(input('Um número menor que 11: '))

    return nume1, nume2
    

    
nume1, nume2 = numeros()

print(nume1)
print(nume2)
while True:
    print('-'*70)
    print('\n Menu de opções:')
    print('1. Soma.')
    print('2. Subtração.')
    print('3. Produto. ')
    print('4. Divisão.')
    print('5. Divisaõ Inteira.')
    print('6. Resto da Divisão.')
    print('7. Sair')

    opcao = int(input('Escreva uma das opções(1 a 7): '))

    if opcao == 1: 
        soma = nume1 + nume2
        print(f'A soma dos dois números vai ser igual {soma}')

    elif opcao == 2:
        subtração = nume1 - nume2
        print(f'O resultado da subtração vai ser {subtração}')

    elif opcao == 3:
        produto = nume1 * nume2
        print(f'A multiplicação desse dois números vai ser igual a {produto}')

    elif opcao == 4:
        divisão = nume1/nume2
        print(f'A divisão do dois números vai ser igual a {divisão}')

    elif opcao == 5:
        divisão_inteira = nume1//nume2
        print(f'A divisão inteira vai ser igual a {divisão_inteira}')

    elif opcao == 6:
        resto_da_divisão = nume1 % nume2
        print(f'o resto da divisão vai ser: {resto_da_divisão}')
    elif opcao == 7:
        print('Saindo do programa...')
        break
    else:
        print(f'opção invalida!!!')



        

    