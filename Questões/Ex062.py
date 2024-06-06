inicio = int(input("Digite o primeiro termo: "))
razão = int(input("Digite a razão: "))
c = 1
t = 11
while c < t:
    print(f"{c}° termo = {inicio}")
    inicio += razão
    c += 1
    if c == t:
        t += int(input("Você quer mostrar mais quantos termos? "))
print(f"Programa finalizado, foram mostrados {c-1}° termos")
