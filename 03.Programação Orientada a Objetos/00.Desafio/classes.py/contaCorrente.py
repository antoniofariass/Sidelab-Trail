from calendar import c
from conta import Conta 


class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, saldo,limite) -> None:
        super().__init__(agencia, numero_conta, saldo)
        self._limite = limite

    def sacar(self,valor):
        return super().sacar()