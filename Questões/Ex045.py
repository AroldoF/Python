from random import choice
from time import sleep


def print_com_delay(texto, delay=0.1):
    for char in texto:
        print(char, end="", flush=True)
        sleep(delay)
    print()


list = ["PAPEL", "TESOURA", "PEDRA"]
print(f"""Game JOKENPO!
Suas opções:
Pedra!
Papel!
Tesoura!\n""")
jogada = input("Escolha sua jogada: ").strip().upper()
bot = choice(list)
if bot == jogada:
    result = "Empate... Quero outra jogo!"
elif (
    (jogada == "PEDRA" and bot == "PAPEL")
    or (jogada == "PAPEL" and bot == "TESOURA")
    or (jogada == "TESOURA" and bot == "PEDRA")):
    result = "HAHA... Eu ganhei!"
else:
    result = "Vo-você deu sorte... Droga eu perdi!"
mensagem = "..."
print_com_delay(mensagem, 0.5)
fala = f"Sua jogada foi {jogada} e a do computador foi {bot}."
print_com_delay(fala, 0.1)
fala = "O computador parece estar pensando numa resposta!"
print_com_delay(fala, 0.1)
print_com_delay(mensagem, 0.5)
fala = f"Computador: {result}"
print_com_delay(fala, 0.1)
fala = "Eu: Será que esse computador não tem nada melhor pra fazer não?"
print_com_delay(fala, 0.1)
print_com_delay(mensagem, 0.5)
fala = "Computador parece envergonhado..."
print_com_delay(fala, 0.1)
