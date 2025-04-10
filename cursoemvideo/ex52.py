#faça um programa que leia um número e diga se ele pe primo
n = int(input('Digite um número: '))
nd = 0
for c in range(1,n+1):
    if n % c == 0:
        nd = nd + 1
if nd == 2:
    print('O número é primo')
else:
    print('O número não é primo')