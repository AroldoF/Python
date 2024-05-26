inicio = int(input("Digite o primeiro termo: "))
razão = int(input("Digite a razão: "))
décimo = inicio + (10 - 1) * razão
for i in range(inicio, décimo + razão, razão):
    print(i)
