class Eletronico:
    def __init__(self,nome) -> None:
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            print(f'{self._nome} já encontrasse ligado.')
            return        
        print(f'{self._nome} foi ligado.')
        self._ligado = True

    def desligar(self):
        if not self._ligado:
            print(f'{self._nome} já encontra-se desligado.')
            return
        self._ligado = False
     