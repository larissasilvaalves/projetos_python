import os 

os.system('cls')

class Operacao:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def valor_a(self):
        return self.a
    
    def valor_b(self):
        self.b

    def valor_c(self):
        self.c
    
    def somar(self):
        soma = self.a + self.b + self.c
        return soma
    



  

a = int(input('O valor de a: '))
b = int(input('Adicione o valor de b: '))
c = int(input('Adicione o valor de c: '))

print


