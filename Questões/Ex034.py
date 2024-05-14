salario=float(input('Digite o salário do funcionário: '))
if salario<=1250:
    new=salario*(15/100)+salario
else:
    new=salario*(10/100)+salario
print('O novo salário será de {}R$'.format(new))