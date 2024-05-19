altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))
imc = peso / (altura**2)
if imc < 18.5:
    grau = "Abaixo do Peso"
elif imc < 25:
    grau = "no Peso Ideal"
elif imc < 30:
    grau = "com Sobre Peso"
elif imc < 40:
    grau = "com Obeaidade"
else:
    grau = "com Obesidade Mórbida"
print(f"De acordo com o seu IMC({imc:.1f}), você está {grau}!")
