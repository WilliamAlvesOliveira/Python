#faça um programa que leia um numero e mostre o seu fatorial usando while
n =  int(input('Digite um número para ver o seu valor fatorial: '))
f = n - 1
print('O valor de \33[32m{}!\33[m é {} x '.format(n,n),end='')
while f > 0:
    print('{}'.format(f),end='')
    if f > 0:
        print(' x ' if f > 1 else ' = ',end='')
    n = n * f
    f = f - 1
print('\33[34m{}\33[m'.format(n))