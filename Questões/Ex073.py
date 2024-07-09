tabela=('Botafogo', 'Flamengo', 'Bahia', 'São Paulo',
'Athletico-PR', 'Atlético-MG', 'Bragantino', 'Palmeiras',
'Internacional', 'Cruzeiro', 'Fortaleza', 'Juventude',
'Grêmio', 'Vasco', 'Corinthians', 'Fluminense',
'Criciúma', 'Atlético-GO', 'Cuiabá', 'Vitória',)

#Mostrando do 1 ao 5 colocado na tabela.
print('\033[34mTimes no G5:', end=' ')
print(tabela[:5])
#Mostrando do 16 ao 20 colocado na tabela.
print('\033[31mTimes no Z4:', end=' ')
print(tabela[-4:])
#Mostrando os times em ordem alfabética!
print('\033[33mTabela em ordem alfebética:', end=' ')
print(sorted(tabela))
#Mostrando em que posição está o Vasco na tabela!
print(f'\033[35mO Vasco esta na {tabela.index('Vasco')+1}° posição na tabela\033[m')

#Outra forma, usando for.
#for cont in range(0,5):
#    print(f'{cont+1}° {tabela[cont]}', end=' ')
#for cont in range(16,20):
#    print(f'{cont+1}° {tabela[cont]}', end=' ')
#for pos, cont in enumerate(sorted(tabela)):
#    print(f'{pos+1}° {cont}', end=' ')
#for pos,count in enumerate(tabela):
#    if 'Vasco' == count:
#        print(f'\033[35mO {count} está na {pos+1}° posição na tabela!\n\033[m')
#        break