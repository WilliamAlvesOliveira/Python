VC = float(input('Qual é o valor da casa? R$ '))
Sal = float(input('Informe o seu salário: R$ '))
P = int(input('Em quantos anos você deseja quitar o financiamento: '))
VP = VC / (P * 12)
if VP <= Sal * 30 / 100:
    print('O valor da parcela será: R$ {:.2f}\nFinanciamento: \33[32mAPROVADO!!!'.format(VP))
else:
    print('Infelizmente o seu financiamento foi: \33[31mNEGADO')
