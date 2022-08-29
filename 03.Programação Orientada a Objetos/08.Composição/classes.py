class Cliente:
    def __init__(self,nome,idade) -> None:
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def inserir_endereco(self,cidade,estado):
        self.enderecos.append(Endereco(cidade,estado)) #esta fazendo a composição ao adicionar atributos da outra classe
    
    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade,endereco.estado) #fazendo uma agregacao
    
     
class Endereco:
    def __init__(self,cidade,estado) -> None:
        self.cidade = cidade
        self.estado = estado