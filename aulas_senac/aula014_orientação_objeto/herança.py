import os

os.system('cls')

import os 

class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def latir(self):
        return "Isto está no método latir()"
    
    def miar(self):
        return "Isto está no método miar()"
    
class Cachorro(Animal):
    def latir(self):
        return f'{self.nome} está latindo!'

class gato (Animal):
    def miar(self):
        return f'{self.nome} está miando!'
    
os.system('cls')
cao = Cachorro('Galileu')
gatinho = gato('Mirty')
print(cao.latir())
print(gatinho.miar())