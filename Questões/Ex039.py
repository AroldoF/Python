from datetime import date
nascimento=int(input('Digite o ano em que você nasceu: '))
idade=date.today().year-nascimento
if idade<18:
    print(f'Ainda não chegou a hora de se alistar, em mais {18-idade} anos')
elif idade==18:
    print(f'Esse ano você completa {idade}, é hora de se alistar!')
else:
    print(f'Já passou em {idade-18} anos da hora de você se alistar, se aliste urgente!')