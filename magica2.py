from random import shuffle

# Matriz [5][5] inicializada com zeros
matriz = [[0 for _ in range(5)] for _ in range(5)]

bombas = int(input("Qual é a quantidade de bombas? "))

if bombas > 25:
    print("A quantidade de bombas não pode ser maior que 25!")
else:
    # Lista linear com bombas (1) e espaços vazios (0)
    lista_bombas = [1] * bombas + [0] * (25 - bombas)

    # Embaralha a lista de bombas
    shuffle(lista_bombas)

    # Converte a lista linear em uma matriz 5x5
    matriz_bombas = [lista_bombas[i : i + 5] for i in range(0, 25, 5)]

    # Exibe a matriz oculta (para testes)
    matriz_amostra = [[0 for _ in range(5)] for _ in range(5)]
    print("Matriz de Bombas (para testes):")
    for linha in matriz_amostra:
        print(linha)

    # Loop do jogo
    while True:
        # Solicita a linha e a coluna
        linha = int(input("Digite a linha (1 a 5): "))
        coluna = int(input("Digite a coluna (1 a 5): "))

        # Verifica se a posição escolhida tem bomba
        if matriz_bombas[linha-1][coluna-1] == 1:
            print("Infelizmente você perdeu!!!")
            print("Matriz final:")
            for linha in matriz_bombas:
                print(linha)
            break
        else:
            print("Por pouco, continue o jogo!")
            # Atualiza a matriz do jogador, mostrando a posição escolhida
            matriz[linha-1][coluna-1] = -1  # Usando -1 para marcar como posição já revelada

        # Exibe a matriz atualizada do jogador
        print("Matriz atual:")
        for linha in matriz:
            print(linha)
