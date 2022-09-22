from pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, idade) -> None:
        super().__init__(nome, idade)
    
    def inserir_conta(self,conta):
        self.conta = conta