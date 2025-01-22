import os 

os.system('cls')

def cadastro_dos_alunos():

    alunos = []

    quantidade_de_alunos = int(input('Quantos aluno iram fazer a matrícula: '))

    for i in range(quantidade_de_alunos):

        print(f'n\Cadastro dos alunos {i+1}')

        nome = input('Nome do aluno: ')
        nascimento = input('Nascimento do aluno: ')
        matricula = input('matrícula:  ')

        aluno = {

            'nome' : nome,
            'nascimento' : nascimento,
            'matrícula' : matricula
        }

        alunos.append(aluno)

    return alunos, quantidade_de_alunos


alunos_cadastrados = cadastro_dos_alunos()



print('\n Cadastro dos alunos vai ser: ')

for aluno in cadastro_dos_alunos : 
    print(f'Nome = {aluno['nome']}, Aluno = {aluno['matrícula']}, nascimento = {aluno['matrícula']} ')

    