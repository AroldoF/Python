num = (
    int(input("Digite um valor: ")),
    int(input("Digite um valor: ")),
    int(input("Digite um valor: ")),
    int(input("Digite um valor: ")),)
print(f"O número 9 aparece {num.count(9)} vezes")
print("O número 3 aparece na", f"{num.index(3)+1}ª posição" if 3 in num else "0ª posição")
print("Os números pares que você digitou são ", end="")
for c in num:
    if c % 2 == 0:
        print(f"{c} ", end="")
