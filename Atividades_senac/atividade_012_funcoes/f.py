#Crie uma função que receba 2 listas: 
#- lista 1: nome, peso, idade 
#- lista 2: John, 40, 1.8
#- Sua função deverá criar um dicionário contendo chave e valor utilizando como base essas duas listas. 
# Depois, seu programa deverá imprimir esse dicionário utilizando uma estrutura de repetição for.

import os 

os.system('cls')

def dicionario(lista_chave, lista_valor):
  
    dic = dict(zip(lista_chave, lista_valor))

    for chave, valor in dic.items():
        print(f'{chave} : {valor}')
        

    return dic


# Invocando a função(NÃO AGUENTO MAIS DEF)

dicionari3 = dicionario(dic)

lista_chave = ["nome", 'peso', 'idade']
lista_valor = ['john', 40, 1.80]




    




