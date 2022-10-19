"""
1- Receber um número inteiro

2- Saber se o número é multiplo de 3 e 5 
    Bacon com ovos

3- Saber se o número NÃO é múltiplo de 3 e 5:
    Passafome 

4- Saber se o número é multiplo sonente de 3:
    Bacon

5- Saber se o número é multiplo sonente de 3:
    Ovos
"""

def bacon_com_ovos(n):
    assert isinstance(n,int), 'n deve ser int'

    if n % 3 == 0: 
        if n % 5 == 0:
            return 'Bacon com ovos'
        else:
            return 'Bacon'
    elif n % 5 == 0:
        return 'Ovos'
    else:
        return 'Passar fome'