from datetime import date

maior = 0
menor = 0
for i in range(1, 8):
    n = int(input(f"Digite a data de nascimento da {i}° pessoa: "))
    idade = date.today().year - n
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f"""{maior} pessoas são maiores de idade!
{menor} pessoas são menores de idade!""")
