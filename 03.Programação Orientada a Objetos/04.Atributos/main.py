class A:
    vc = 123 #variavel de classe

    def __init__(self) -> None:
        self.vc = 321 #variavel de instancia

a1 = A()
a2 = A()

print(a1.vc)
print(a2.vc)

a1.vc = 3211 #criando um atributo direto na instancia

print(a1.__dict__)
print(a2.__dict__)


print(a1.vc)
print(a2.vc)

A.vc = 'Alterado' #utilizar a mudança com a classe para termos efeito
print(A.vc)
