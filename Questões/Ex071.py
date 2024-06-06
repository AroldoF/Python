n = int(input("Digite o valor do saque: "))
c50 = c20 = c10 = c1 = 0
s = n
while True:
    if s >= 50:
        s -= 50
        c50 += 1
    elif s >= 20:
        s -= 20
        c20 += 1
    elif s >= 10:
        s -= 10
        c10 += 1
    elif s >= 1:
        s -= 1
        c1 += 1
    if s == 0:
        break
print(f"Você solicitou o saque de {n:.2f}R$, o valor será entregue em")
print(f"{c50} notas de 50R$")
print(f"{c20} notas de 20R$")
print(f"{c10} notas de 10R$")
print(f"{c1} notas de 1R$")