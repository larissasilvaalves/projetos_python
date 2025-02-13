import os 
os.system('cls')
class Matricula: 
    def __init__(self, nome, nascimento, cpf, cidade):
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.cidade = cidade


        #solicitando informações
nome = input('Adicione o nome do aluno: ')
nascimento = int(input('Data de nascimento: '))
cpf = input('CPF: ')
cidade = input('Escreva o nome da cidade: ')
#finalizando o programa 
os.system('cls')
matriculado = Matricula(nome, nascimento, cpf, cidade)
print('-'*70)
print('Matrícula do aluno: ')
print(f'Nome do aluno: {matriculado.nome}')
print(f'Data de nascimento: {matriculado.nascimento}')
print(f'Cpf do aluno: {matriculado.cpf}')
print(f'Cidade do atual(Natal): {matriculado.cidade}')