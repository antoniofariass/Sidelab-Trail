from conta import Conta


class ContaPoupanca(Conta):
    def __init__(self, agencia, numero_conta, saldo) -> None:
        super().__init__(agencia, numero_conta, saldo)

    def sacar(self):
        return super().sacar()