from datetime import date
aa = date.today().year
print('\33[34m~'*32)
print('\33[36mConfederação Nacional de Natação\33[m')
print('\33[34m~\33[m'*32)
print('Informe a sua data de nascimento')
d = int(input('Dia: '))
m = int(input('Mes: '))
a = int(input('Ano: '))
if aa - a <= 9:
    print('{} Anos, categoria: Mirim'.format(aa - a))
elif aa - a <= 14:
    print('{} Anos, categoria: Infantil'.format(aa - a))
elif aa - a <= 19:
    print('{} Anos, categoria: Júnior'.format(aa - a))
elif aa - a <= 25:
    print('{} Anos, categoria: Sênior'.format(aa - a))
else:
    print('{} Anos, categoria: Master'.format(aa -  a))
