# A empresa "RootCalc" está desenvolvendo um software de cálculo de raízes de equações
#  quadráticas para auxiliar engenheiros e cientistas em suas análises e projetos.
#  Eles precisam de um programa que calcule as raízes da equação quadrática 𝑥²−6𝑥+5 
# sem depender de funções ou métodos predefinidos, utilizando apenas os conceitos e 
# operações básicas aprendidos até o momento. Essas raízes são conhecidas
#  como 𝑥’ = 5 e 𝑥’’ = 1, e o programa deve ser capaz de calcular essas raízes de 
# forma precisa, seguindo os princípios matemáticos fundamentais.

import os

os.system ('cls')

#declaração

a = 1
b = -6
c = 5

delta = (b**2) - (4* a * c)
print('-'*70)
#print(delta)

raiz_primaria = ((-b) + (delta**(1/2))) / 2 * a
raiz_secundaria = ((-b) -(delta**(1/2))) / 2 * a
print('-'*70)
print(raiz_primaria)
print(raiz_secundaria)