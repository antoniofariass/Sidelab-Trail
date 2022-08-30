class Pessoa:
    def __init__(self,nome,idade) -> None:
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} Falando...')

class Cliente(Pessoa): #fazendo com que herde de Pessoa os atributos
    def comprar(self):
        print(f'{self.nomeclasse} comprando...')

class Aluno(Pessoa):
    pass

#SOBREPOSIÇÃO

class ClienteVIP(Cliente): #herda cliente que herda de pessoa 
    def falar(self): #sobrepondo o metodo falar que ele herdou da classe Pessoa
        
        super().falar #utilizando do comando super para ir na superclasse pegar o metodo falar
                      #se a Classe cliente tivese o metodo falar, ela seria a superclasse
        
        #Pessoa.falar(self), chama um metodo de uma classe que herda especifica
        
        print('Outra coisa qualquer.')

    def __init__(self, nome, idade, sobrenome) -> None: #atribuindo novos metodos e utilizando o mesmo construtor da superclasse
        Pessoa.__init__(self,nome, idade) #se usar super.__init__, utilizara o construtor da superclasse dela, nesse caso, Cliente
        self.sobrenome = sobrenome
        print(f'{self.nome} {self.sobrenome}')
