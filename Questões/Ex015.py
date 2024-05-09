dias = int(input("Quantos dias o carro foi alugado?"))
km = float(input("Quantos km o carro alugado percorreu?"))
valor = (dias * 60) + (km * 0.15)
print("O valor a pagar será {:.2f}R$".format(valor))
