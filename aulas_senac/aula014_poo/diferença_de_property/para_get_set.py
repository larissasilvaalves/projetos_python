import os 

os.system('cls')

class Minha_classe:
    def __init__(self, valor):
        self._atributo = valor

    def get_atributo(self):
        return self._atributo
    
    def set_atributo(self):
        return self._atributo
    
obj = Minha_classe(10)
# O atributo trabalha como uma função
obj.set_atributo(20) 
# Saída como função 
print(obj.get_atributo())