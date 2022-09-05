""" Declarar um método como abstrato é uma forma de obrigar o programador a redefinir esse método em todas as subclasses para as quais deseja criar objetos. """

from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def falar(self):
        pass

class B(A): #so podera instanciar a classe B quando tiver o metodo falar
    def falar(self):
        print('Falando.... B...')


a = A() #error pois nao consegue instanciar uma classe abstrata