from random import choice

a1 = input("Informe o nome do Aluno: ")
a2 = input("Informe o nome do Aluno: ")
a3 = input("Informe o nome do Aluno: ")
a4 = input("Informe o nome do Aluno: ")
alunos = [a1, a2, a3, a4]
print("O aluno(a) sorteado foi {}".format(choice(alunos)))
