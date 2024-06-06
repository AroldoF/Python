soma = mil = menor = 0
while True:
    nome = input("Digite o nome do produto: ")
    produto = float(input("Digite o valor do produto: R$"))
    s = " "
    soma += produto
    if produto > 1000:
        mil += 1
    if produto < menor or menor == 0:
        menor = produto
        barato = nome
    while s not in "NnSs":
        s = input("Quer continuar? [S/N] ").strip()[0]
    if s in "Nn":
        break
print(f"Total da compra foi {soma:.2f}R$")
print(f"{mil} produtos acima de 1000R$!")
print(f"O produto mais barrato se chama {barato} e custa {menor:.2f}R$!")
