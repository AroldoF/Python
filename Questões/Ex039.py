from datetime import date

nascimento = int(input("Digite o ano em que você nasceu: "))
idade = date.today().year - nascimento
if idade < 18:
    print(f"Você tem {idade} anos, ainda não chegou a hora de se alistar, em mais {18-idade} anos")
    print(f"Seu alistamento será em {date.today().year+(18-idade)}")
elif idade == 18:
    print(f"Esse ano você completa {idade}, é hora de se alistar!")
else:
    print(f"Você tem {idade} anos, já passou em {idade-18} anos da hora de você se alistar!")
    print(f"Seu alistamento deveria ter sido em {date.today().year-(idade-18)}")
