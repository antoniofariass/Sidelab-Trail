'''
public, protected, private

_ -> protected (por recomendação, ao se ver uma variavel assim, nao acessa-la)

__ -> privado (o programa vai proibir de ser acessado)
    porem caso vc tente usar, ira criar um atributo com o mesmo nome

'''

class BaseDeDados:
    def __init__(self) -> None:
        self.__dados = {}

    @property #liberar o acesso a um atributo por um getter
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id,nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
       for id, nome in self.__dados['clientes'].items():
            print(id,nome)
    
    def apaga_cliente(self,id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Otavio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')

bd.__dados = 'Outra coisa' #cria um atributo de mesmo nome
print(bd.__dados)

print(bd._BaseDeDados__dados) #acessa o atributo real da classe

bd.lista_clientes()

#utilizar o setter para mexer no atributo, nao ir diretamente nele se nao ira criar uma copia