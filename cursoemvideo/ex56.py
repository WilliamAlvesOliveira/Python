#desenvolva um programa que leia o nome, o sexo, e a idade de 4 pessoas
# no final mostre: a nedia de idade do grupo, o nomedo homem mais velho
#e quantas mulheres tem menos de 20 anos
Mv = 0
mi = 0
nm = 0
ti = 0
for c in range(1,5):
    n = str(input('Nome da {}ª pessoa: '.format(c)))
    i = int(input('Qual é a idade do/da {}: '.format(n)))
    s = int(input('Qual é o sexo do/da {}: \n\33[31m[1]\33[mMasculino\n\33[31m[2]\33[mFeminino\nopção: '.format(n)))
    ti = ti + i
    if s == 1:
        if i > Mv:
            Mv = i
            nMv = n
    if s == 2:
        if i < 21:
            nm = nm + 1
print('A média de idade do grupo foi :{}'.format(ti / 4))
print('O nome do homem mais velho é {}, com {} anos'.format(nMv,Mv))
print('O número de mulheres com menos de 21 anos é: {}'.format(nm))
