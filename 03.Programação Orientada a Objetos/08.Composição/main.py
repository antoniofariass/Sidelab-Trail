from classes import Cliente, Endereco

cliente1 = Cliente('Luiz',32)
cliente1.inserir_endereco('Belo Horizonte','MG')

cliente2 = Cliente('Maria', 55)
cliente2.inserir_endereco('Salvador','BA')
cliente2.inserir_endereco('Rio de Janeiro', 'RJ')

cliente3 = Cliente('João',19)
cliente3.inserir_endereco('São Paulo', 'SP')

print(cliente1.nome)
cliente1.lista_enderecos()

print(cliente2.nome)
cliente2.lista_enderecos()

print(cliente3.nome)
cliente3.lista_enderecos()

print("___________________")

