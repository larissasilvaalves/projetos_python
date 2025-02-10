#Crie um programa que peça ao usuário 2 números maiores que 0 e menores que 11. 
#Depois mostre um menu com as seguintes operações:
#1. Soma: 2. Subtração : 3. Produto : 4. Divisão : 5. Divisão inteira : 6. 
#Resto da divisão.
#O usuário deverá escolher um número maior ou  igual a 1 e menor ou igual a 6. 
#Em seguida, você criará funções que retornem os resultados das operações, imprimindo os resultados na tela.
import os
os.system('cls')
class operacoes: 
    def __init__(self, soma, subtracao, produto, divisao, divisão_inteira, resto_da_divisao):  #método construtor
        self.soma = soma
        self.subtracao = subtracao
        self.produto = produto                                  #atributos
        self.divisao = divisao
        self.divisao_inteira = divisão_inteira
        self.resto_da_divisao = resto_da_divisao


#programa principal
nume1 = int(input('Adicione um número maior que 0: '))
nume2 = int(input('O segundo número tem que ser menor que 11: '))
if nume2 > 11: 
    print('O número é maior que 11!, escreva um número menor que 11!')
    exit()
    #O exit() é uma função em Python que termina a execução de um programa de forma imediata. 
    #Quando chamada, ela encerra o programa, independentemente de onde for executada.
os.system('cls')
#operações
soma = nume1 + nume2
subtracao = nume1 - nume2
produto = nume1*nume2
divisao = nume1/nume2
divisão_inteira = nume1//nume2
resto_da_divisao = nume1 % nume2

#funcionameto
print('-'*70)
print('Finalizando o programa...')
print(f'Soma: {soma}')
print(f'Subtração: {subtracao}')
print(f'Produto: {produto}')
print(f'Divisão: {divisao}')
print(f'Divisão inteira: {divisão_inteira} ')
print(f'Resto da divisão: {resto_da_divisao}')


#Referência à instância: O self é uma referência à instância atual da classe. Isso significa que quando você cria um 
#objeto a partir de uma classe, o self se refere a esse objeto específico.
#Acessando atributos e métodos: 
#Ele permite que você acesse e modifique os atributos e métodos de uma instância particular da classe, 
#garantindo que cada objeto tenha seus próprios valores e comportamentos.