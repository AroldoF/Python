n = 0
soma = 0
c=0
while n != 999:
    n = int(input(f"Digite o {c+1}° número: "))
    if n == 999:
        print('Programa encerrado!')
        break
    soma += n
    c+=1
print(f'Todos os {c} números somado são igual a {soma}')