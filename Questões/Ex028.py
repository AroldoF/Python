from random import randint

num = int(input("Digite um número de 0 a 5: "))
n = randint(0, 5)
if num == n:
    print("Parabéns, você acertou! o número realmente era {}".format(n))
else:
    print("Você errou, o número era {}".format(n))
