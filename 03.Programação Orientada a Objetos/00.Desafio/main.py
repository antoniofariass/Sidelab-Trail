from classes.banco import Banco
from classes.conta import Conta , ContaCorrente , ContaPoupanca
from classes.cliente import Cliente
from classes.pessoa import Pessoa


banco = Banco()

cliente1 = Cliente('Antonio',18)
cliente2 = Cliente('Maria',37)
cliente3 = Cliente('Lucas', 58)

conta1 = ContaPoupanca(1111,254136,0)
conta2 = ContaCorrente(2222,254137,0)
conta3 = ContaPoupanca(1212,254138,0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(40)
    cliente1.conta.sacar(20)
else:
    print('Cliente não autenticado!')

banco.inserir_clientes(cliente1)
banco.inserir_conta(conta1)

banco.inserir_clientes(cliente2)
banco.inserir_conta(conta2)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(40)
    cliente1.conta.sacar(20)
else:
    print('Cliente não autenticado!')

if banco.autenticar(cliente2):
    cliente1.conta.depositar(40)
    cliente1.conta.sacar(20)
else:
    print('Cliente não autenticado!')