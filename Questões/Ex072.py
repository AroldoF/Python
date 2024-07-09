tupla = ("zero","um","dois","três","quatro","cinco","seis","sete",
        "oito","nove","dez","onze","doze","treze","catorze","quinze",
        "dezesseis","dezessete","dezoito","dezenove","vinte")
while True:
    num=int(input('Digite um número entre 0 e 20: '))
    if num > 0 and num < 20:
        print(f'Você digitou {tupla[num].capitalize()}!')
        break
    print(f'\033[31mErro!\033[m O número \033[31m{num}\033[m não está nos paremetros de medida!')