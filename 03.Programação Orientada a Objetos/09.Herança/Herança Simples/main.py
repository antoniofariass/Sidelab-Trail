from classes import *

c1 = Cliente('Luiz',45)
print(c1.nome)

a1 = Aluno('João',79)
print(a1.nome)

a1.falar()
c1.falar()

c2 = ClienteVIP('Rose',30,'Miranda')
c2.falar()