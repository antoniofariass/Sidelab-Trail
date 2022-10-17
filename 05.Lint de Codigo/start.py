def soma(a,b):
    c = a+b
    return c 

#snake-case 
def soma(num_1,num_2):
    soma_dois_numeros = num_1 + num_2
    return soma_dois_numeros

#docstring
def soma(num_1:int, num_2:int) -> int:
    """Somando dois números
    :param - num_1: primeiro numero da soma
             num_2: segundo numero da soma 
    :return soma_dois_numeros
    """

    soma_dois_numeros = num_1 + num_2
    return soma_dois_numeros

Soma = soma(1,2)
