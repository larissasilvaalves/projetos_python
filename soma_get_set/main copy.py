import os 
#criando minnha classe:
class Soma:
    def __init__(self, a, b):
       self._a = a
       self._b = b

    @property
    def a(self):
        return self._a
    @property
    def b(self):
        return self._b
    
    @a.setter
    def a(self, a):
       self._a = a
    
    @b.setter
    def b(self, b):
        self._b = b

    def somar(self):
       return self._a + self._b
    

#corpo principal
soma = Soma(0, 0)

soma.a = 90
soma.b = 876
print(soma.somar())

