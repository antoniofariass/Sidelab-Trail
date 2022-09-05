class TaErradoError(Exception): #criar um error que nao tenha no Exception
    pass

def testar():
    raise TaErradoError('Errado!')

try:
    testar()
except TaErradoError as error:
    print(f'Erro: {error}')