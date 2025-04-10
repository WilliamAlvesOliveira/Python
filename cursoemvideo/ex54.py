##crie um programa que leia o ano de nascimento de sete pessias
#no final mostre quantas pessoas não atingiram a maioridade  e quantos ja são maiores
from datetime import date
ano = date.today().year
p = 0
for c in range(1,8):
    a = int(input('Digite a ano de nascimento da {}ª pessoa: '.format(c)))
    if ano - a >= 21:
        p = p + 1
print('Destas pessoas {} atingiram a maioridade'.format(p))
print('As outras {} pesspas ainda são menores de idade'.format(c-p))
