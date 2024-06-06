from random import randint

c = 0
print(f"Vamos jogar Par ou Ímpar?!")
while True:
    esc = input("Par ou ímpar?[P/I] ").strip().upper()[0]
    if esc not in "PpIi":
        print("Erro! Digite novamente:")
        continue
    n = int(input("Digite o valor que você quer joga: "))
    pc = randint(0, 10)
    soma = pc + n
    print(f"Você jogou {n} e o Computador jogou {pc}. O total foi {soma} ", end="")
    print("deu par!" if soma % 2 == 0 else "deu ímpar!")
    if (soma % 2 == 0 and esc == "I") or (soma % 2 != 0 and esc == "P"):
        break
    else:
        c += 1
        print("Eba! Você ganhou!")
print(f"Game Over... Ganhou {c} seguidas")
