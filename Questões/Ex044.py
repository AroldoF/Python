compras = float(input("Digite o valor das compras: R$"))
print("""Formas de pagamento:
Digite [1] à vista dinheiro!
Digite [2] à vista no cartão!
Digite [3] 2x no cartão!
Digite [4] 3x ou mais no cartão!""")
escolha = int(input("Sua escolha: "))
print(f"De acordo com a forma de pagamento:")
if escolha == 1:
    pg = compras - (compras * 10 / 100)
    print(f"Você terá 10% de desconto, assim o preço final será de R${pg:.2f}")
elif escolha == 2:
    pg = compras - (compras * 5 / 100)
    print(f"Você terá 5% de desconto, assim o preço final será de R${pg:.2f}")
elif escolha == 3:
    pg = compras
    pgm = compras / 2
    print(f"Você não terá descontos, assim o preço final será de R${pg:.2f} e as parcelas mensais serão de R${pgm:.2f}")
elif escolha == 4:
    pg = compras + (compras * 20 / 100)
    p = int(input("Digite o total de parcelas: "))
    pgm = pg / p
    print(f"Você terá 20% de juros, assim o preço final será de R${pg:.2f} e as parcelas mensais serão de R${pgm:.2f}")
else:
    print('Opção Inválida!')