sexo = input(f"Digite seu gênero:[M/F] ").strip()[0]
while sexo not in "MmFf":   
    sexo=input("Erro! Informe seu gênero: ").strip()[0]
print(f'Seu gênero {sexo.upper()[0]} registrado com sucesso!')