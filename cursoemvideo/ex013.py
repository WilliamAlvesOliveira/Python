sal = float(input('Qual é o salário do funcionaria R$: '))
aum =sal + sal/100*15
print('O funcionario que ganhava R$ {:.2f}\ncom 15% de aumento passará a receber R$ {:.2f}'.format(sal,aum))