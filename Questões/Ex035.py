reta1 = float(input("Digite uma reta: "))
reta2 = float(input("Digite uma reta: "))
reta3 = float(input("Digite uma reta: "))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("É possivel formar um triângulo!")
else:
    print("Não é possivel formar um triângulo!")
