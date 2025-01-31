import os 

os.system('cls')
#ZeroDivisorError
try:
    resultado = 10/0
except ZeroDivisionError:
    print('Erro: Divisão por zero!')

#ValueError
try:
    numero = int('não é um número')
except ValueError:
    print('Erro: Valor inválido!')

#TypeError
try:
    soma = '5' + 5
except TypeError:
    print('Erro: Tipo de dado incompatível')

#IndexError
lista = [ 1 ,2, 3]
try:
    item = lista[5]
except IndexError:
    print('Erro: Índice fora do intervalo da lista!')

#KeyError
dicionario = {'chave': 'valor' }
try:
    valor = dicionario['chave_inexistente']
except KeyError:
    print('Erro: Chave não encontrada no dicionário')

#FileNotError

try:
    with open('arquivo_inexistente.txt','r') as arquivo:
        conteudo = arquivo.read()
except FileExistsError:
    print('Error: Arquivo não encontrado!')

#IOError
try:
    with open('arquivo_inexistente.txt ','r') as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print('Erro: Operação de E/S falhou!')

try:
    with open ('arquivo.txt', 'w') as  arquivo:
        conteudo = arquivo.read()
except IOError:
    print('Erro: Operação de E/S falhou!')

    
#atrribueError
class exemplo():
    def _init(self):
        self.atributo = "valor"

objeto = exemplo ()
try:
    print(objeto.atributo_inesxistente)
except AttributeError:
    print('erro: Atributo não encontrado no objeto!')

#importError
try:
    import modulo_inexistente
except ImportError:
      





      