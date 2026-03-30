print('\33[34m======================================\33[m')
print('\33[36m           CALCULADORA IMC            \33[m')
print('\33[34m======================================\33[m')
peso = float(input('Informeo seu peso: '))
altura = float(input('Informa a sua altura: '))
IMC = peso / (altura ** 2)

print('Seu IMC é de : \33[34m{:.1f}\33[m'.format(IMC))
if IMC < 18.5:
    print('\33[31mVpcê está \33[4mABAIXO\33[0;31m do peso!\33[m')
elif IMC >= 18.5 and IMC <25:
    print('\33[32mVocê esta na faixa de peso ideal\33[m')
elif IMC >= 25 and IMC  <30:
    print('\33[33mVocê esta com \33[4mSOBREPESO\33[m')
elif IMC >= 30 and IMC < 40:
    print('\33[4;31mOBESIDADE\33[M')
else:
    print('\33[30;41mOBESIDADE MÓRBIDA!!!!\33[m')