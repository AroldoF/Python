h = c = m = 0
while True:
    idade = int(input("Digite sua idade: "))
    sexo = " "
    while sexo not in "MmFf":
        sexo = input("Digite seu Gênero:[M/F] ").strip()[0]
    if idade >= 18:
        c += 1
    if sexo in "Mm":
        h += 1
    elif sexo in "Ff" and idade < 20:
        m += 1
    s = " "
    while s not in "SsNn":
        s = input("Você quer cadastrar mais pessoas? [S/N] ").strip()[0]
    if s in "Nn":
        break
print(f"Pessoas acima dos 18 anos: {c}")
print(f"Homens cadastrados: {h}")
print(f"Mulheres abaixo dos 20 anos: {m}")
