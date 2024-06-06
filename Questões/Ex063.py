r = int(input("Digite um número: "))
n1 = 0
n2 = 1
c = 2
print(f"{n1} -> {n2}", end=" -> ")
while c < r:
    n3 = n1 + n2
    print(n3, end=" -> ")
    c += 1
    n1 = n2
    n2 = n3
print("Fim")
