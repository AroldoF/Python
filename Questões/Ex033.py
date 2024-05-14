n1 = float(input("Digite o primeiro número! "))
n2 = float(input("Digite o segundo número! "))
n3 = float(input("Digite o terceiro número! "))
if n1 >= n2 and n1 >= n3:
    maior = n1
elif n2 >= n1 and n2 >= n3:
    maior = n2
else:
    maior = n3
if n1 <= n2 and n1 <= n3:
    menor = n1
elif n2 <= n1 and n2 <= n3:
    menor = n2
else:
    menor = n3
print("Seu maior número é {}".format(maior))
print("Seu menor número é {}".format(menor))

# Jeito mais fácil de fazer!
# print(min(n1,n2,n3))
# print(max(n1,n2,n3))
