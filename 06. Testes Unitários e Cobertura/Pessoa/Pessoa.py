import requests

class Pessoa:
    def __init__(self,nome,sobrenome) -> None:
        self._nome = nome
        self._sobrenome = sobrenome
        self._dados = False 
    
    def obter_todos_os_dados(self):
        resposta = requests.get('https://jsonplaceholder.typicode.com/users/1')

        if resposta.ok:
            self._dados = True
            return 'CONECTADO'
        else:
            return 'ERRO 404'