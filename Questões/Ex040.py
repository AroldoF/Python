n1 = float(input("Digite uma nota: "))
n2 = float(input("Digite uma nota: "))
m = (n1 + n2) / 2
if m < 5:
    s = "REPROVADO"
elif m < 7:
    s = "em RECUPERAÇÃO"
else:
    s = "APROVADO"
print(f"De acordo com a média {s}, o aluno está {m:.1f}")
