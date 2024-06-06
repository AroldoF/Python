soma = c = 0
while True:
    n = int(input(f"Digite o {c+1}° número:(999 para parar): "))
    if n == 999:
        print("Programa encerrado!")
        break
    soma += n
    c += 1
print(f"Todos os {c} números somado são igual a {soma}")
