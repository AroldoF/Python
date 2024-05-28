n = int(input("Digite um número: "))
c = 0
new = 1
ne = 1
while c < n - 1:
    new *= n - c
    c += 1
print(f"{n}! é igual a {new}")
