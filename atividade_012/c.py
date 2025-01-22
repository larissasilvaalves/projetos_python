#Crie uma função que verifica se uma aluno(a) está cadastrado ou não em um dicionário. 
# Se estiver cadastrado, imprima o nome desse aluno e o resto dos seus dados. 
# O dicionário deverá conter nome, matrícula e a data de nascimento do aluno.

import os 

os.system('cls')

matriculados = { "Davi" : "2008-D2345",
             "Fernanda" : "2007-F5668",
             "Paulo" : "2009-P2309",
             'Marcos' : "2009-M5643",
             'Bruna'  : "2008-B3290",
             'Shamyra' : '2008-S2345'
                
            }

def matriculado():

        nome = input('Digite o nome do aluno que deseja achar: ')
        if nome in matriculados:
            print(f'O aluno {nome} está no cadastro, matrícula: {matriculados[nome]}')
        else:
            print(f'O aluno não foi matriculado.')

        return nome, matriculados

matriculado()

