l1 = float(input('Digite a medida do 1º lado do triângulo: '))
l2 = float(input('Digite a medida do 2º lado do triângulo: '))
l3 = float(input('Digite a medida do 3º lado do triângulo: '))
if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:
    print('Essas medidas \33[1;32mformam\33[m um triângulo', end=' ')
    if l1 == l2 and l2 == l3:
        print('\33[1;4;34mEquilatero\33[m')
    elif l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
        print('\33[1;4;34mIsosceles')
    else:
        print('\33[1;4;34mEscaleno\33[m')
else:
    print('Essas medidas \33[1;31mNÂo\33[m formam um triângulo')