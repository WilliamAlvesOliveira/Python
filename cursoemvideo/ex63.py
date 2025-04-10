#esceva um programa que mostre um numero n inteiro e mostre os n primeiros números de uma sequencia de fibonacci
print('==============================')
print('    sequencia de Fibonacci    ')
print('==============================')
c = 2
n1 = 0
n2 = 1
n = int(input('Quantos números da sequência você deseja ver: '))
if n == 1:
    print(n1)
elif n == 2:
    print('{} {}'.format(n1,n2))
elif n > 2:
    print ('{} {}'.format(n1,n2),end=' ')
    while c != n:
        n3 = n1 + n2
        print(n3,end=' ')
        n1 = n2
        n2 = n3
        c += 1
print('\nFim')
