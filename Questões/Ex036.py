casa = float(input("Digite o valor da casa; R$"))
salario = float(input("Digite o seu salário: R$"))
anos = int(input("Em quantos anos você pretende pagar a casa? "))
valor_mensal = casa / (anos * 12)
max_parcela = salario * 30 / 100
if valor_mensal <= max_parcela:
    print("Parabéns, sua comprar da casa foi aprovada!")
    print(f"Você pagará pacerlas de {valor_mensal:.2f} mensalmente durante {anos} anos!")
else:
    print(
        f"Infelizmente sua compra não foi aprovada,pois as parcelas ficariam {valor_mensal:.2f} que excederia 30% do salário!"
    )
