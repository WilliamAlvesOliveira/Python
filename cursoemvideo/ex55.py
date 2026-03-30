#faça um programa que leia o peso de cinco pessoas
#no final, mostre qual foi o maior e o menos peso
Mp = 0
mp = 999.99
for c in range(1,6):
    n = str(input('Digite o nome da {}ª pessoa: '.format(c)))
    p = float(input('Di''gite o peso do/da {}: '.format(n)))
    if p > Mp:
        Mp = p
        nMp = n
    if p < mp:
        mp = p
        nmp = n
print('O maior peso foi do/da {}, com {}kg'.format(nMp,Mp))
print('O menor peso foi do/da {}, com {}kg'.format(nmp,mp))
