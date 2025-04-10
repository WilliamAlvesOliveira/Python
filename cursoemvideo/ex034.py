sal = float(input('Qual é o salário do funcionário? R$'))
if sal <= 1250.00:
    aum = sal/100 * 15
else:
    aum = sal/100 * 10
print('O funcionário passará a ganhar \33[32mR${:.2f}'.format(sal+aum))
