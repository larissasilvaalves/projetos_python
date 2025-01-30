import os 

os.system('cls')

try:

    resultado = 10/0
    arquivo = open('arquivo_inesxitente.txt','r')
except ZeroDivisionError:
    print('Erro: Divisão por zero!')
except FileExistsError:
    print('Erro: Arquivo não encontrado!')
except Exception as e:
    print(f'Erro inesperado: {e}')

print('Continua a execuçaõ do programa.')
