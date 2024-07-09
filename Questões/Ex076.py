produtos=('Lápiz', 1.75,
          'Canetas', 22.30,
          'Livro', 34.90,   
          'Estojo', 25,
          'Caderno', 15.90,
          'Transferidor', 4.20,
          'Compasso', 9.99,
          'Mochila', 120.32,
          'Borracha',2)
print(f'{'Lojinha':^36}')
for pos in range(len(produtos)):
    if pos%2==0:
        print(f'{produtos[pos]:-<30}',end='')
    else:
        print(f'R${produtos[pos]:.2f}')
