palavras = ("simplesmente", "colecionador", "avassalador", "preposto", "medicamento")
for c in palavras:
    print(c, end="")
    for itens in c:
        if itens in 'aeiou':
            print(f' {itens}',end='')
    print()
