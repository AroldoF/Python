from random import randint

print("Computador: acabei de pensar em um número entre 0 e 10!")
print("Computador: Por que não tenta adivinhar?")
jogador = int(input("Sua escolha: "))
pc = randint(0, 10)
c = 0
while jogador != pc:
    if pc > jogador:
        print("Computador: \033[31mErrou!\033[m porque não tenta um número \033[35mMAIS ALTO? \033[m")
    elif pc < jogador:
        print("Computador: \033[31mErrou!\033[m porque não tenta um número \033[35mMAIS BAIXO? \033[m")
    jogador = int(input("Sua escolha: "))
    c += 1
print(f"Computador: \033[34mParabéns!\033[m O número que pensei também era \033[33m{pc}\033[m")
print(f"O número de palpites usados foi de \033[33m{c}\033[m vezes")
