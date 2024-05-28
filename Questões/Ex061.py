inicio = int(input("Digite o primeiro termo: "))
razão = int(input("Digite a razão: "))
c = 1
while c < 11:
    print(f"{c}° termo = {inicio}")
    inicio += razão
    c += 1
