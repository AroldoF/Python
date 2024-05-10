from math import hypot

c1 = float(input("Digite um cateto: "))
c2 = float(input("Digite um cateto: "))
h = hypot(c1, c2)
print("Sua hipotenusa é igual a {:.2f}".format(h))
