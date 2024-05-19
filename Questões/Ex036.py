p_casa=float(input('Digite o valor da casa; '))
salario=float(input('Digite o seu salário: '))
anos=int(input('Em quantos anos você pretende pagar a casa? '))
valor_mensal=p_casa/(anos*12)
max_parcela=salario*30/100
if valor_mensal<max_parcela:
    print('Parabéns, sua comprar da casa foi aprovada!')
    print(f'Você pagará pacerlas de {valor_mensal} mensalmente durante {anos} anos!')
else:
    print('Infelizmente sua compra não foi aprovada!')