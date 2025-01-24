import os
import math

#entrada

numero1 = float(input('entre com um número: '))
numero2 = float(input(' entre com outro numero: '))

#processamento

divisão = numero1/numero2

arredondar_para_cima = math.ceil(numero1+numero2)
arrendondar_para_baixo = math.floor(divisão/numero1+numero2)


#saída

print('-'*50)
print(f'a divisão é {divisão}')
print(f'o numero arredondada para baixo é {arrendondar_para_baixo}')
print(f'o numero arredondado para cima é {arredondar_para_cima}')
print('='*50)










