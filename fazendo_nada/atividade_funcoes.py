#Você vai criar um programa em Python que simula um sistema de cadastro de produtos.
# O programa deve ter uma função para cadastrar os produtos e uma função para exibir
# todos os produtos cadastrados.

import os 

os.system('cls')

def cadastro_de_produtos():

    produtos = input('Quantos produtos você deseja adicionar: ')
    produtos = int(produtos)

    for i in range (produtos):
        nomes = input('Adicione o nome do produto: ')
        lista_de_produtos = cadastro_de_produtos.append(nomes)
        print(lista_de_produtos)

        return lista_de_produtos
    






    