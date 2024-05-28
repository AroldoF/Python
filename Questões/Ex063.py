r = int(input("Digite um número: "))
n1 = 0
n2 = 1
c = 1
print(n1,'aqui e n1')
while c < r:
    n3 = n1 + n2
    if c<r:
        print(n2,'aqui e n2')
        c += 1
    if c<r:
        print(n3,'aqui e n3')
        c += 1
    n1=n3
    n2=n3+n2