from abc import ABC, abstractmethod


class Conta:
    def __init__(self,agencia,conta,saldo) -> None:
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self,valor):
        if not isinstance(valor, (int,float)):
            raise ValueError('Saldo precisa ser númerico.')
        self._saldo = valor

    def depositar(self,valor):
        if not isinstance(valor, (int,float)):
            raise ValueError('Depósito precisa ser númerico.')
        
        self.saldo += valor
    
    def detalhes(self):
        print(f'Agencia: {self.agencia}', end=' | ')
        print(f'Conta: {self.conta}', end='\n')
        print(f'Saldo: {self.saldo}')
        
    @abstractmethod
    def sacar(self,valor):
        pass
