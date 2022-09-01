from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def falar(self):
        pass

class B(A): #so podera instanciar a classe B quando tiver o metodo falar
    def falar(self):
        print('Falando.... B...')


a = A() #error pois nao consegue instanciar uma classe abstrata