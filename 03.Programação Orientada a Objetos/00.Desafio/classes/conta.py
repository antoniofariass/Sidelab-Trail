from abc import ABC, abstractmethod


class Conta:
    def __init__(self,agencia,numero_conta,saldo) -> None:
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def numero_conta(self):
        return self._numero_conta

    def depositar(self,valor):
        self._saldo += valor

    def detalhes(self):
        print(f'Agência: {self.agencia}\n'
              f'Conta: {self.numero_conta}\n'
              f'Saldo: {self.saldo}')
    
    @abstractmethod
    def sacar(self,valor): pass
    
    
class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, saldo,limite=100) -> None:
        super().__init__(agencia, numero_conta, saldo)
        self._limite = limite

    @property
    def limite(self):
       return self._limite

    def sacar(self,valor):
        if (self.saldo + self.limitevalor) < valor:
            print('Saldo insuficiente!')
            return
        
        self._saldo -= valor
        self.detalhes()


class ContaPoupanca(Conta):
    def sacar(self,valor):
        if self.saldo < valor:
            print('Saldo insuficiente!')
            return
        
        self._saldo -= valor
        self.detalhes()