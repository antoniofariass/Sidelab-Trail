class Produto:
    def __init__(self,nome,preco):
        self.nome = nome #inicializa com o setter | self._nome = nome, so incializa o nome
        self.preco = preco
    
    def desconto(self, percentual):
        self.preco = self.preco - ((percentual/100) * self.preco)

    #Getter - nome
    @property
    def nome(self):
        return self._nome

    #Setter - nome
    #nao posso ter setter sem getter, pode ter getter sem setter
    @nome.setter
    def nome(self, palavra):
        self._nome = palavra
    
    #Getter - preco
    @property
    def preco(self):
        return self._preco

    #Setter - preco
    @preco.setter
    def preco(self,valor):
        if isinstance(valor,str):
            valor = float(valor.replace('R$',''))
        self._preco = valor

p1 = Produto('Camiseta',50)
p1.desconto(10)
print(p1.preco)

p2 = Produto('Caneca','R$15')
p1.desconto(20)
print(p2.preco)
