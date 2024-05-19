num = int(input("Digite um número: "))
escolha = int(
    input(
        "Digite 1 para converter para binário, 2 paraconverter para octal e 3 para converter para hexadecimal!"
    ))
if escolha == 1:
    nome = "Binário"
    convertido = bin(num)
elif escolha == 2:
    nome = "Octal"
    convertido = oct(num)
elif escolha == 3:
    nome = "Hexadecimal"
    convertido = hex(num)
print(f"Seu valor {num} convertido para {nome}, seria igual a {convertido[2:]}.")
