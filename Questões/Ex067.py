while True:
    n = int(input("Quer ver a tabuada de qual valor? "))
    if 0 > n:
        break
    for i in range(1, 11):
        print(f"{n} x {i:2} = {n*i}")
print("Programa encerrado")
