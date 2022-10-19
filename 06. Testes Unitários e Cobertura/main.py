from calculadora import soma

#ASSERTION 
try:
    print(soma(15,20))
except AssertionError as e:
    print(f'Conta invalida! {e}')
