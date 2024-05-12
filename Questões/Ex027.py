nome = input("Digite seu nome completo! ").strip().title()
cut = nome.split()
print("Prazer em te conhecer!")
print("Seu primeiro nome é {}!".format(cut[0]))
print("Seu último nome é {}!".format(cut[len(cut) - 1]))

# Outra forma de Resolução!
# e=nome.rfind(' ')+1
# print('Prazer em te conhecer!')
# print("Seu primeiro nome é {}!".format(cut[0]))
# print("Seu último nome é {}!".format(nome[e::]))
