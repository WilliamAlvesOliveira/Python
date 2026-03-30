from datetime import date
aa = date.today().year
print('\33[32m===\33[33m========\33[34m====\33[33m=======\33[32m===\33[m')
print('\33[1;42m  \33[1;43mEXÉ1RCIT\33[1;44m0  \33[1;44mBRA\33[1;43mSILEIRO\33[1;42m  \33[m')
print('\33[32m===\33[33m========\33[34m====\33[33m=======\33[32m===\33[m')
print('Informe sua data de nacimento')
d = int(input('Dia: '))
m = int(input('Mes: '))
a = int(input('Ano: '))
if aa - a == 18:
    print('Idade: {} anos'.format(aa-a))
    print('Você precisa se alistar no exército brasileiro')
    print('Ano de alistamento: {}'.format(a+18))
elif aa - a > 18:
    print('Idade: {} anos'.format(aa-a))
    print('Você ja deveria ter se alistado há: {} anos'. format(aa - (a + 18)))
    print('Ano de alistamento {}'.format(a + 18))
else:
    print('Idade {}: anos'.format(aa - a))
    print('Ainda falta {} anos para você precisar se alistar!'.format(18-(aa-a)))
    print('Ano de alistamento será: {}'.format(a + 18))
