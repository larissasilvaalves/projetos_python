#Crie uma função que receba a altura e  peso de uma pessoa. Depois retorne o seu IMC.
import os 

os.system('cls')

def pesoaltura():

    peso = float(input('Adicione seu peso(em kg): '))
    altura = float(input('Adicione sua altura(em metros): '))

    return peso, altura

peso, altura = pesoaltura()

divisao = peso/ (altura**2)

print(f'Sua altura é {altura}(metros), e seu peso é de {peso}kg')
print(f'Seu IMC equivale a:{divisao: .2f}')
