limite = 80
multa  = 7.00
vel = float(input('Qual é a velocidade atual do carro?km/h: '))
if vel <= limite:
    print('Siga viagem! Tenha um bom dia!')
else:
    print('O limite da via é de {}km/h'.format(limite))
    print('Você esta acima do limite de velocidade')
    print('Sua multa é de {:.2f} R$'.format((vel-limite)*multa))
