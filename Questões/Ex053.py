frase = input("Digite uma frase:\n").strip().upper().split()
frase = "".join(frase)
new = frase[::-1]
# Outra forma:
# new = ""
# for i in range(len(frase)-1, -1, -1):
# new += frase[i]
print(f"Sua frase {frase} ao contrario é {new}!")
if frase == new:
    print("Sua Frase é um Palíndromo!")
else:
    print("Sua Frase não é um aplíndromo!")
