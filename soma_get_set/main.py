import os 
#criando minnha classe:
class Soma:
    def __init__(self, a, b):
       self._a = a
       self._b = b

    def get_a(self):
        return self._a
    
    def get_b(self):
        return self._b
    
    def set_a(self, a):
       self._a = a
    
    def set_b(self, b):
        self._b = b

    def somar(self):
       return self._a + self._b
    

#corpo principal
soma = Soma()

soma.set_a(31)
soma.set_b(14)

