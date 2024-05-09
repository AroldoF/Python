s = float(input("Qual é o salário do funcionário? R$"))
novo = s + (s * 15 / 100)
print(
    "O salário de {:.2f}R$ com o aumento de 15% ficará com um salário de {:.2f}R$!".format(s, novo))
