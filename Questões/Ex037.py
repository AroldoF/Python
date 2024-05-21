num = int(input("Digite um número: "))
print("""Digite um número: 
[1] para converter para binário! 
[2] paraconverter para octal! 
[3] para converter para hexadecimal!""")
escolha = int(input("Sua opção: "))

if escolha == 1:
    nome = "Binário"
    convertido = bin(num)
elif escolha == 2:
    nome = "Octal"
    convertido = oct(num)
elif escolha == 3:
    nome = "Hexadecimal"
    convertido = hex(num)
else:
    print('Opção Inválida')
print(f"Seu valor {num} convertido para {nome}, seria igual a {convertido[2:]}.")
