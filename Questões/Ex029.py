v = float(input("Digite a velocidade do veículo: "))
if v > 80:
    m = (v - 80) * 7
    print("O veículo estava em {}Km, acima do limite permitido de 80km.".format(v))
    print("Você será multado em {:.2f}R$".format(m))
else:
    print("Você estava dentro do limite de velocidade!")
print('Tenha um bom dia!')
