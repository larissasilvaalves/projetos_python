import os 
from datetime import datetime

class Usuario:
    def __init__(self, nome, data_nascimento):
        #chama o setter para definir o nome
        self.set_nome(nome)
        #chama o setter para definir a data de nascimento
        self.set_data_nascimento(data_nascimento)

    def get_nome(self):
        #retorna a data de nascimento do usuário
        return self._nome
    
    def get_data_nascimento(self):
        #retorna a data de nascimento do usuário
        return self.get_data_nascimento
    
    def set_data_nascimento(self, data_nascimento):
        #define ua nova variável para a data de nascimento
        self._data_nascimento = data_nascimento

        #calcule a idade do usuário
        #obtém a data e hora atuais
        hoje = datetime.now()

        # Converter a data de nascimento de strig para um objeto datetime
        nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
        #calcula a idade subtraindo o ano de nascimento do ano atual e 
        #ajusta se a data de aniversário ainda não ocorreu neste ano
        self._idade = hoje.year - nascimento.year - \
            ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
        
        def get_idade(self):
            #retorna a idade do usuário
            return self._idade
        
os.system('cls')
print('-'*70)
print('Programa para encontrar idade')
print('='*70)
nome = input('Digite seu nome: ')
data_nascimento = input('Data de nascimento "dd/mm/yyyy":  ')
 
#cria uma instância da classe Usuário
usuario = Usuario(nome, data_nascimento)

#exibe o nome, data de nascimento e idade do usuário
print('-'*70)
print(f'Nome: {usuario.get_nome()}')
print(f'Data de nascimento: {usuario.get_data_nascimento()}')
print(f'Idade: {usuario.get_idade()} anos')
print('-'*70)
        