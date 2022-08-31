class A:
    def falar(self):
        print('Falando... Estou em A.')

class B(A):
    def falar(self):
        print('Falando... Estou em B.')

class C(A):
    def falar(self):
        print('Falando... Estou em C.')

class D(B,C): #fazendo uma herança multipla, 
              #começa da esquerda para direita caso tenha o problema do diamante
    pass

d1 = D()
d1.falar()
    
