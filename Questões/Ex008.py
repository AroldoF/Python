m = float(input("Digite um valor em metros!"))
lista = [1000, 100, 10, 0.1, 0.01, 0.001]
uni = ["Km", "Hm", "Dam", "Dm", "Cm", "Mm"]
for i, n in zip(lista, uni):
    if i > 3:
        convertido = m / i
    else:
        convertido = m / i
    print("Convertendo {}M para {} temos que {}{}".format(m, n, convertido, n))
