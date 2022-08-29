class Pessoa:
    def __init__(self,nome,idade) -> None:
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} Falando...')

class Cliente(Pessoa): #fazendo com que herde de Pessoa os atributos
    pass

class Aluno(Pessoa):
    pass
