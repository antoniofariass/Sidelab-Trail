class MinhaClasse:
    '''Documentação normal'''

    atributo = 1
    atributo2 = 'Valor'

    def __init__(self,texto) -> None:
        '''Inicializa os dados
        
        :param texto: o texto da classe
        :type texto: str
        '''

        self.texto = texto
        self.exibe_texto(texto)

        @staticmethod 
        def exibe_texto(texto):
            '''Metodo que exibe um texto de 100 caracteres na tela
            
            :param texto: Um texto de 100 caracteres
            :type texto: str

            :return: o texto de 100 caracteres
            
            :raises ValueError: se o texto tiver mais que 100 caracteres
            :raises TypeError: se o texto não for uma string 
            '''

            if not isinstance(texto,str):
                raise TypeError('texto precisa ser uma string')
            
            if len(texto) > 100:
               raise ValueError('texto precisa ter 100 caracteres ou menos')

            return texto 