#Crie um programa que pergunte o ano de nascimento do usuário e calcule sua idade atual.
import datetime
import os
os.system('cls')

def retornar_idade():
    ano_nascimento = int(input('Adicione o seu ano de nascimento: '))
    agora = datetime.datetime.now()
    ano_atual = agora.year
    idade = ano_atual - ano_nascimento
    return idade

#date time, utilizado para informar nosso ano, dia, hora atual.

#conta de matématica para descobrir sua idade
idade = retornar_idade()

print('Agora iremos descobrir sua idade...')
print(f'Você tem {idade}')
