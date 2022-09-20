from pessoa import Pessoa
from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca

class Cliente(Pessoa):
    def __init__(self, nome, idade) -> None:
        super().__init__(nome, idade)
    
    #ver como implementar
    def informacao_cliente(self):
        return self.ContaCorrente