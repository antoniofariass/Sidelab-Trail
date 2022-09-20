from abc import ABC, abstractmethod


class Conta:
    def __init__(self,agencia,numero_conta,saldo) -> None:
        self._agencia = agencia
        self._numero_conta = numero_conta
        self.__saldo = saldo

    
    def deposito(self,valor):
        self.__saldo =+ valor

    @abstractmethod
    def sacar(self):
        pass
    
    
