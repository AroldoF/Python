from random import shuffle, choice

# Inicializar os montes e o baralho
monte1 = [0] * 13
monte2 = [0] * 13
monte3 = [0] * 13
monte4 = [0] * 13

# montes = [
#     [0] * 13 for _ in range(4)
# ]
baralho = [i for i in range(1, 53)]  # Baralho global


def embaralhar():
    m1 = m2 = m3 = m4 = c = 0
    for i in baralho:
        if c == 0:
            monte1[m1] = i
            m1 += 1
        elif c == 1:
            monte2[m2] = i
            m2 += 1
        elif c == 2:
            monte3[m3] = i
            m3 += 1
        else:
            monte4[m4] = i
            m4 += 1
        c += 1
        if c == 4:
            c = 0


def novo_baralho():
    global baralho  # Permite modificar a variável global baralho
    escolha = int(input("Em qual monte está sua carta? (1, 2, 3 ou 4) "))
    if escolha == 1:
        baralho = monte2 + monte3 + monte4 + monte1
    elif escolha == 2:
        baralho = monte1 + monte3 + monte4 + monte2
    elif escolha == 3:
        baralho = monte1 + monte2 + monte4 + monte3
    else:
        baralho = monte1 + monte2 + monte3 + monte4


shuffle(baralho)
print("Baralho embaralhado:", baralho)

carta_escolhida = choice(baralho)
print("Escolha uma carta:")

for rodada in range(3):
    print(f"\nRodada {rodada + 1}:")

    embaralhar()

    print("Monte 1:", monte1)
    print("Monte 2:", monte2)
    print("Monte 3:", monte3)
    print("Monte 4:", monte4)

    novo_baralho()

# Finalizar o jogo após o loop de jogadas
print("\nFim do jogo. Sua carta é:")
print(baralho[-1])
