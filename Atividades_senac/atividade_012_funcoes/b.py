import os 

os.system('cls')

def cadastro_dos_alunos():

    alunos = []
    quantidade_de_alunos = int(input('Quantos alunos iram fazer a matrícula: '))
    for i in range(quantidade_de_alunos):
        print(f'n\Cadastro dos alunos {i+1}')
        nome = input('Nome do aluno: ')
        nascimento = input('Nascimento do aluno: ')
        matricula = input('Matrícula:  ')
        aluno = {

            'nome' : nome,
            'nascimento' : nascimento,
            'matrícula' : matricula
        }

        alunos.append(aluno)

    return alunos, quantidade_de_alunos


alunos_cadastrados = cadastro_dos_alunos()

print('\n Cadastro dos alunos vai ser: ')
for aluno in alunos_cadastrados: 
    print(f'Sua lista de {aluno}')
    print(f'Nome = {aluno["nome"]}, Aluno = {aluno["matrícula"]}, nascimento = {aluno["nascimento"]}')
