soma = 0
maior = 0
menor = 0
c = 0
r = "Ss"
while r not in "Nn":
    n = int(input(f"Digite o {c+1}° número: "))
    if maior < n:
        maior = n
    if menor > n or c == 0:
        menor = n
    soma += n
    c += 1
    if c % 2 == 0 and c > 1:
        r = input("Você quer continuar?[S/N] ")
media = soma / c
print(f"A média de todos os {c} números é {media}")
print(f"Entre os {c} números o maior foi {maior} e o menor foi {menor}")
