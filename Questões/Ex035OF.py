#Exercício 035,mas usando '-'.
reta1 = input("Digite uma reta: ")
reta2 = input("Digite uma reta: ")
reta3 = input("Digite uma reta: ")
lista = [reta1, reta2, reta3]
r1 = 0
r2 = 0
r3 = 0
for i in lista:
    for j in i:
        if j == "-":
            if i == reta1:
                r1 += 1
            elif i == reta2:
                r2 += 1
            else:
                r3 += 1
maior = max(r1, r2, r3)
m1 = min(r1, r2, r3)
m2 = min([r for r in [r1, r2, r3] if r != m1])
if maior < (m1 + m2):
    print("É possivel formar um triângulo!")
else:
    print("Não é possivel formar um triângulo!")
