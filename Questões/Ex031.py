d = float(input("Digite a Quantidade de Km da sua viagem: "))
if d <= 200:
    pay = d * 0.5
else:
    pay = d * 0.45
print("Pelos {}Km rodados, o valor a pagar é {:.2f}R$".format(d, pay))
