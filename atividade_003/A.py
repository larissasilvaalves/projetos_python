import math
import os
os.system('cls')

#entrada
 
numero= int(input('entre com um número: '))

#resolução
raiz_quadrada =  math.sqrt(numero)
print(f'A raiz quadrada de {numero} é {raiz_quadrada}')

#procesamento
aredondar_para_cima = math.ceil(numero)
arrendondar_para_baixo = math.floor(numero)

