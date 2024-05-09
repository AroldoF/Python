n = int(input("Digite um valor!"))
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in lista:
    print("{} X {:2} = {}".format(n, item, n * item))
