from math import sin, cos, tan, radians

an = float(input("Digite um ângulo: "))
se = sin(radians(an))
co = cos(radians(an))
ta = tan(radians(an))
print("Seu Seno é igual a {:.2f}".format(se))
print("Seu Cosseno é igual a {:.2f}".format(co))
print("Sua Tangente é igual a {:.2f}".format(ta))
