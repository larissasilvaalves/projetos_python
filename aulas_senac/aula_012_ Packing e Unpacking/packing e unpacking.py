import os 

os.system('cls')


def empacotar (*lista_numeros):
    print(f'empacotados: {lista_numeros}')
    for i in lista_numeros:
        print(f'empacotados: {i}')


empacotar(1 ,2, 3, 4, 5)


def desempacotar (a, b, c, d, e):
    print('desempacotados: ')
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')
    print(F'd = {d}')
    print(f'e = {e}')


lista_numeros = [1, 2, 3, 4, 5 ]
desempacotar(*lista_numeros)

def empacotar_dicionario (**dados_do_dicionario):
    print(f'Dados do dicionario : {dados_do_dicionario}')
    for k , v in dados_do_dicionario.items():
        print(f'chave = {k}, valor = {v}')


print('-'*30)
print('Dicionário...')
print( nome = 'juquinha', idade = 23, peso = 70.5  )



def desempacotar_dicionario(nome, idade, peso):
    print(f'nome = {nome}')
    print(f'idade = {idade}')
    print(f'peso = {peso}')


dicionario = dict(nome = 'Maria', idade = 16, peso = 50)
desempacotar_dicionario(dicionario)
print()