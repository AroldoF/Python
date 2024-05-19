n1=float(input('Digite o primeiro valor: '))
n2=float(input('Digite o segundo valor: '))
if n1>n2:
    valor=('maior')
elif n1==n2:
    valor=('igual')
else:
    valor=('menor')
print(f'Seu primeiro valor {n1} é {valor} que seu segundo valor {n2}!')