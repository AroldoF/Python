s = 0
n1 = float(input("Digite o 1° número: "))
n2 = float(input("Digite o 2° número: "))
while s != 5:
    print("=" * 40)
    print(
        """[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa"""
    )
    print("=" * 40)
    s = int(input("Sua escolha: "))
    if s == 1:
        print(f"\033[33mO número {n1} + {n2} = {n1+n2}\033[m")
    elif s == 2:
        print(f"\033[33mO número {n1} * {n2} = {n1*n2}\033[m")
    elif s == 3:
        print(f"\033[33mO maior número entre {n1} e {n2} e igual {max(n1,n2)}\033[m")
    elif s == 4:
        n1 = float(input("Digite o 1° número: "))
        n2 = float(input("Digite o 2° número: "))
