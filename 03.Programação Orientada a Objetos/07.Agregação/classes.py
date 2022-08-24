from mailbox import NotEmptyError


class CarrinhoDeCompras:
    def __init__(self) -> None:
        self.produtos = []
    
    def inserir_produto(self,produto):
        self.produtos.append(produto)
    
    def lista_produto(self):
        for produto in self.produtos:
            print(produto.mome, produto.valor) #utilizando atributos da outra classe 
        
    def soma_total(self):
        total_carrinho = 0
        for produto in self.produtos:
            total_carrinho += produto.valor
        return total_carrinho



class Produto:
    def __init__(self,nome,valor) -> None:
        self.nome = nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self,valor):
        self.__valor = valor 