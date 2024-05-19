from datetime import date

nasc = int(input("Informe o ano em que você nasceu: "))
idade = date.today().year - nasc

if idade <= 9:
    categoria = "MIRIM"
elif idade <= 14:
    categoria = "INFANTIL"
elif idade <= 19:
    categoria = "JUNIOR"
elif idade <= 20:
    categoria = "SÊNIOR"
else:
    categoria = "MASTER"
print(f"A categoria que você consegue competir é {categoria}!")

"""
test=bool(False)
list=[9,14,19,20]
new=['MIRIM','INFANTIL','JUNIOR','SÊNIOR']
for x,y in zip(list,new):
    if idade<=x:
        test=True
        print(f'A categoria que você consegue competir é {y}!')
        break
if test==False:
    print(f'A categoria que você consegue competir é MASTER!')
"""
