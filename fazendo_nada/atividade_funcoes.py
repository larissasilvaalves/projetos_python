#Você vai criar um programa em Python que simula um sistema de cadastro de produtos.
# O programa deve ter uma função para cadastrar os produtos e uma função para exibir
# todos os produtos cadastrados.

import os 

os.system('cls')

cadastro_de_produtos = []

def cadastro():

    quantidade_produtos = int(input('Adicione a quantidade de produtos: '))

    for i in range (quantidade_produtos):
        print (f'Cadastro dos produtos {i+1}')
        produto = input('Adicione o nome do produto: ')
        valor = float(input('Valor do produto: '))
        compras = { 'produto':{produto},'valor': {valor}}

        cadastro_de_produtos.append(compras)

        return cadastro_de_produtos
    



cadastro_de_produtos = cadastro()

print(cadastro_de_produtos)







print(cadastro)
    