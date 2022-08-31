from eletronico import Eletronico
from log import LogMixin

class Smartphone(Eletronico,LogMixin):
    def __init__(self, nome) -> None:
        super().__init__(nome)
        self._conectado = False 
    
    def conectar(self):
        if not self._ligado:
            info = f'{self._nome} não está ligado.'
            print(info)
            self.log_info(info)
            return

        if self._conectado:
            error = f'{self._nome} Já está conectado.'
            print(error)
            self.log_error(error)
            return
        
        info = f'{self._nome} foi conectado.'
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} não está conectado.'
            print(error)
            self.log_error(error)
            return
        
        info = f'{self._nome} foi desligado com sucesso.' 
        print(info)
        self.log_info(info)
        self._conectado = False