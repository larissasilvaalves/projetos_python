#  A empresa "DataMax" está desenvolvendo um novo 
# software de análise estatística e precisa de uma 
# funcionalidade que permita aos usuários inserir três 
# números e, em seguida, exibir na tela qual é o maior número,
#  qual é o menor número ou se os números são todos iguais. 
# Essa funcionalidade é crucial para os analistas de dados da "DataMax" que
#  trabalham com conjuntos de dados diversos e precisam rapidamente 
# identificar as características básicas desses conjuntos, 
# como a presença de outliers ou a uniformidade dos números.

import os 

os.system('cls')

#ENTRADA

a = int(input('coloque um número: '))
b = int(input('coloque um número: '))
c = int(input('coloque um número: '))

#RESPOSTAS
if a > b and a > c:
    print(f'{a} é o ser o maior numero')
    print('-'*70)
else:
    print(f'{a} é menor que {b} e {c}')

if b > a and b > c :
    print(f'{b} é o número maior entre {a} e {c}')
else: 
    print(f'{b} é menor que {a} e {c}')

if c > a and c > b :
    print(f'{c} é o maior númeo entre {a} e {b}')
else:
    print(f'{c} é menor que {a} e {b}')
