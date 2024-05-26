n = int(input("Digite um número: "))
soma = 0
for i in range(1, n + 1):
    if n % i == 0:
        soma += 1
        print(f"\033[34m{i}\033[m", end=" ")
    else:
        print(f"\033[31m{i}\033[m", end=" ")
# Verifica se a soma de divisores é 2
if soma == 2:
    print(f"\nSeu número \033[33m{n}\033[m é primo")
else:
    print(f"\nSeu número \033[33m{n}\033[m não é primo")
