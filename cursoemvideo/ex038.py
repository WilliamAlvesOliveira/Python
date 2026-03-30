n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 == n2:
    print('Ambos os números são \33[33;4mIguais\33[m')
elif n1 < n2:
    print('O maior número é \33[32;4m{}\33[m'.format(n2))
    print('e o menor é \33[31;4m{}\33[m'.format(n1))
else:
    print('O maior número é \33[4;32m{}\33[m'.format(n1))
    print('e o menor é \33[4;31m{}\33[m'.format(n2))
