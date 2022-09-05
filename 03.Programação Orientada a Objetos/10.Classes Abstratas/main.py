from classes.contaPoupanca import ContaPoupanca
from classes.contaCorrente import ContaCorrente

cp = ContaPoupanca(1111,2222,0)
cp.depositar(10)
cp.detalhes()
cp.sacar(10)

print('################')

cc = ContaCorrente(1111,3333,0,500)
cc.detalhes()
cc.depositar(100)
cc.sacar(50)