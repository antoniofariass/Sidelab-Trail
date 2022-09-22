class Pessoa:
    def __init__(self, nome,idade) -> None:
        self._nome = nome
        self._idade = idade

    #getter nome
    @property
    def nome(self):
        return self.nome

    #getter idade 
    @property
    def idade(self):
        return self.idade

    
    