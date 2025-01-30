#Elabore um programa que receba quatro notas de um aluno e calcule a média dessas notas.

#imports
import os 

os.system('cls')
notas_dos_alunos = []
#funções

def calcular_media(media_total):
    media_total = sum(notas_dos_alunos) / len(notas_dos_alunos)

    return media_total

#programa principal


for i in range(4):
    nota = float(input('qual a nota do aluno: '))
    notas_dos_alunos.append(nota)
    os.system('cls')
    print(notas_dos_alunos)


#invocar função
resultado = calcular_media(notas_dos_alunos)
print(f'A média total das notas vai ser {resultado}')