media = 0
mv = 0
velho = 0
for i in range(1, 5):
    print("-" * 5, f"{i}° pessoa", "-" * 5)
    nome = input("Digite seu nome: ").strip().upper()
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu gênero [M/F]: ").strip().upper()
    media += idade
    if idade > velho and sexo == "M":
        velho = idade
        hv = nome
    elif idade < 20 and sexo == "F":
        mv += 1
print(f"A média de idade do grupo é {media/4}")
# testando se tem homem no programa:
if velho != 0:
    print(f"Homem mais velho se chama {hv.capitalize()}!")
else:
    print("Não teve homem mais velho!")
print(f"A quantidade dee mulheres abaixo dos 20 anos é {mv}")
