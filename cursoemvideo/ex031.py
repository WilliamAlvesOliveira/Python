km = float(input('Sua viagem tem a distanci de quantos kn: '))
if km <200:
    valor = km * 0.50
else:
    valor = km* 0.45
print('Sua viagem é de {} km\nO valor da sua passagem será de {:.2f} R$'.format(km,valor))
