i = 1
s = "Ss"
while s not in "Nn":
    sexo = input(f"Digite o gênero do {i}° [M/F]: ")
    if sexo not in "MmFf":
        print("Erro! Gênero não identificado.")
        i -= 1
    print("=" * 20)
    i += 1
    s = input("Quer continuar?[S/N]\n").upper()
