#faça um programa que leia seis números inteiros e mostre a soma apenas dos pares
s = 0
for c in range(1,7):
    n = int(input('Digite o {}º valor: '.format(c)))
    if n %2 ==0:
        s = s + n
print('A soma dos valores pares foi {}.'.format(s))