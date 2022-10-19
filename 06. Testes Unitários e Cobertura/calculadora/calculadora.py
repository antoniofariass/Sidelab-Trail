#ASSERTION
def soma(x,y):
    assert isinstance(x,(int,float)), 'X precisa ser um inteiro ou float' #rodar o progrma sem assertion " -O python nome_do_arquivo.py "
    return x + y

#DOCTEST
def soma(x,y):
    """ Soma x e y
    
    >>> soma(10,20)
    30

    >>> soma(-10,20)
    10

    >>> soma('10',20)
    Traceback (most recent call last):
     
    AssertionError: x precisa ser int ou float.
    """

    return x + y 

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    doctest.testmod(verbose=True)