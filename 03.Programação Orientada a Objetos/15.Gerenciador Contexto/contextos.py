class Arquivo:
    def __init__(self,arquivo,modo) -> None:
        print('abrindo arquivo')
        self.arquivo = open(arquivo,modo)
    
    def __enter__(self):
        print('retornando arquivo')
        return self.arquivo
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        print('fechando arquivo')
        self.arquivo.close()
        #tratei a exceção
        return True
    

with Arquivo('abc.txt','w') as arquivo:
    arquivo.write('Alguma coisa')


###############################################################

#fazendo a mesma coisa de antes com uma função

from contextlib import contextmanager

@contextmanager
def abrir(arquivo,modo):
    try:
        arquivo = open(arquivo,modo)
        yield arquivo
    finally:
        arquivo.close()