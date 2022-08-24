from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta', 50)

print(p1.nome)
print(p1.valor)

p1.valor = 60 

print(p1.valor)
print(p1.__dict__)




