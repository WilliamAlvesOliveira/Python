#crie um programa que leia  que leia varios n inteiros e só pare quando o usuáriodigitar o numero 999
#no fim mostre quantos números foram digitados e a soma deles desconsiderando o 999
n = s =  q = 0
while n != 999:
    n = int(input('Digite um número (999 para \33[4msair\33[m): '))
    if n != 999:
        s = s + n
        q = q + 1
print('A soma dos {} números digitados foi de {}.'.format(q,s))