from random import  randint
from time import sleep

lista = ('Pedra', 'Papel', 'Tessoura')
print('\33[36m         JOKENPO!\33[m')
print('\33[34m-=\33[m'*13)
op = int(input('''\33[31m[1]\33[mPara jogar \33[4mPedra\33[m
\33[31m[2]\33[mPara jogar \33[4mPapel\33[m
\33[31m[3]\33[mPara jogar \33[4mTessoura\33[m
Selecione a sua opção: '''))
com = randint(1,3)

sleep(0.5)
print('\33[34m-=\33[m'*13)
print('\33[1;35mJO...',end='')
sleep(0.7)
print('\33[1;33mKEN...\33[m',end='')
sleep(0.7)
print('\33[1;;32mPO!!!!!!\33[m')
sleep(0.5)
print('\33[34m-=\33[m'*13)

if op == com:
    print('\33[1;34mPlayer\33[m {} \33[31mx\33[m {} \33[1;34mComputer\33[m'.format(lista[op-1],lista[com-1]))
    print('\33[33;4mEmpate!\33[m')
elif op == 1 and com == 2 or op == 2 and com == 3 or op == 3 and com == 1:
    print('\33[1;34mPlayer\33[m {} \33[31mx\33[m {} \33[1;34mComputer\33[m'.format(lista[op-1],lista[com-1]))
    print('Você \33[4;31mPERDEU!\33[m')
elif op == 1 and com == 3 or op == 2 and com == 1 or op == 3 and com == 2:
    print('\33[1;34mPlayer\33[m {} \33[31mx\33[m {} \33[1;34mComputer\33[m'.format(lista[op-1],lista[com-1]))
    print('Você \33[4;32mVENCEU!')
else:
    print('\33[31mJOGADA INVALIDA!!!\33[m')
