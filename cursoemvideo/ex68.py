#faça um programa que jogue par ou impar. o programa para quanod o jogador
#perder mostrando quantas vitórias consecutivas ele venceu
from random import randint
from time import sleep
v = 0
while True:
    print('--- PAR OU IMPAR ---')
    j = str(input('Escolha Par ou Impar: ')).upper().strip()[0]
    while j not in 'PI':
        print('\33[31mOpçãp onvalida!\33[m')
        j = str(input('Escolha Par ou Impar: ')).upper().strip()[0]
    n = int(input('Selecione o número que você jogará [1 à 10]: '))
    print('Jogador:', end='')
    print('\33[34mPar \33[m' if j == 'P' else'\33[36mImpar \33[m ',end='')
    print(n)
    sleep(0.5)
    print('Computador: ',end='')
    c = randint(1,10)
    print('\33[34mPar \33[m' if j == 'I' else '\33[36mImpar \33[m ',end='')
    print(c)
    sleep(1)
    s = n + c
    print(f'\33[34mJogador \33[m ',end='')
    print('PAR x ' if j == 'P' else 'IMPAR x ',end='')
    print('IMPAR 'if j == 'P' else 'PAR ',end='')
    print(f'\33[35mComputador\33[m')
    if s % 2 == 0:
        r = 'P'
    else:
        r = 'I'
    print(f'Resultado {s} ',end='= ')
    print('\33[34mPar.\33[m' if r == 'P' else '\33[36mImpar.\33[m')
    sleep(1.5)
    if r == j:
        v += 1
        print('\33[32mParabéns!\33[m Você venceu\nQuero revanche.')
        sleep(1)
    else:
        print('\33[31mVocê perdeu!\33[m')
        break
print(f'Resultado\nNúmero de vitórias consecutivas {v}')
