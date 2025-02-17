import os 

os.system('cls')

import math
import os 

class Triangulo:
    def __init__(self, cateto_1, cateto_2):
        self.cateto_1 = cateto_1
        self.cateto_2 = cateto_2


class TrianguloRetangulo(Triangulo):
    def calcular_hipotenusa(self):
        resultado = math.sqrt(pow(self.cateto_1, 2)) + pow(self.cateto_2, 2)
        return resultado
    
while True:
    os.system('cls')
    cateto_1 = int(input('Entre com o cateto 1: '))
    cateto_2 = int(input('Entre com o cateto 2: '))

    if cateto_1 == 0 or cateto_2 == 0:
        print('Fim do programa!')
        break       
    else:
        triangulo_retangulo = TrianguloRetangulo(cateto_1, cateto_2)
        hipotesuna = triangulo_retangulo.calcular_hipotenusa()

    os.system('cls')

    print(f'O triangulo retangulo de lado 1 = {cateto_1}')
    print(f'{cateto_2} é igual  hipotenusa {hipotesuna:.2f} aproximadamente')
    print(f'Pressione enter para retornar')