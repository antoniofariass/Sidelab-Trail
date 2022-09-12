"""
EM PYTHON TUDO É UM OBJETO: incluindo classes
Metaclasses são as "Classes" que criam classes
type é uma metaclasse (!!!???)
"""
class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs,name,bases,namespace)
        
        if 'b_fala' not in namespace:
            print(f'Oi, voce precisa criar o metodo de fala em {name}')
        else:
            if not callable(namespace['b_fala']):
                print(f'b_fala precisa ser um método em {name}')
        
        return type.__new__(mcs,name,bases,namespace)

class A(metaclass = Meta):
    def fala(self):
        self.b_fala()
    
class B(A):
    # b_fala = 'valor'
    def b_fala(self):
        print('Oi')
