import os 

os.system('cls')



inicio = int(input('entre com o inicio: '))
fim = int(input('entre com o fim: '))


for i in range(inicio, fim):
    
    divisor = 0
    for c in range(1, i + 1):
        if i % c == 0: 

            divisor += 1
            soma =+ i
   
    if divisor == 2:

     print(f'O número {c} é um número primo ')


print()

