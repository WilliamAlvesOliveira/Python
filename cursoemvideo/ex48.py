#faça um programa que calcule a soma entre todos os números impares
#que são multiplos de 3 e que acontecem em um intervalo de 1 até 500
s = 0
n =0
for c in range(1,501, 2):
    if c %3 == 0:
        n = n + 1
        s = s + c
print('A soma dos {} valores impares multiplos de 3 é {}'.format(n,s))