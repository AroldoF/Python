r1 = float(input("Digite uma reta: "))
r2 = float(input("Digite uma reta: "))
r3 = float(input("Digite uma reta: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        t = "Equilátero"
    elif r1 == r2 or r1 == r3 or r2 == r3:
        t = "Isósceles"
    else:
        t = "Escaleno"
    print(f"É possivel formar um triângulo {t}!")
else:
    print("Não é possivel formar um triângulo!")
