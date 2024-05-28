from random import randint

s = False
c = 0
while s != True:
    pc = randint(0, 10)
    jogador = int(input("Digite um número de 0 a 10:\033[33m "))
    if pc == jogador:
        s = True
        print(f"\033[34mParabéns!\033[m O número que o computador pensou foi \033[33m{pc}\033[m")
    else:
        c += 1
        print(f"\033[31mQue pena!\033[m O computador escolheu \033[33m{pc}\033[m")
    print('=' * 48)
print(f"O número de palpites usados foi de \033[33m{c}\033[m vezes")
