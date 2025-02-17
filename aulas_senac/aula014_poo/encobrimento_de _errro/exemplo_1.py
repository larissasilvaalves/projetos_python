import os 

os.system('cls')

try:
    #código que pode gerar várias exceções
    resultado = 10/0
    arquivo = open('arquivo_inesxixtente.txt' ,'r')
except Exception:

    pass

print("Continua a execução do programa.")