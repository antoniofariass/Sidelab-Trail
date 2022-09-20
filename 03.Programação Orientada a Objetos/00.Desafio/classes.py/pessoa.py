class Pessoa:
    def __init__(self, nome,idade) -> None:
        self.nome = nome
        self.idade = idade

    #getter nome
    @property
    def nome(self):
        return self.nome

    #getter idade 
    @property
    def idade(self):
        return self.idade

    
    