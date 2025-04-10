from random import randint
from time import sleep

print('\33[36m         JOKENPO!\33[m')
print('\33[34m-=\33[m'*13)
print('\33[31m[1]\33[mpara jogar \33[4mPEDRA\33[m')
print('\33[31m[2]\33[mpara jogar \33[4mPAPEL\33[m')
print('\33[31m[3]\33[mpara jogar \33[4mTESOURA\33[m')
jogador = int(input('Qual opção você ira jogar: '))

if jogador == 1:
    jogesc = 'PEDRA'
elif jogador == 2:
    jogesc = 'PAPEL'
elif jogador == 3:
    jogesc = 'TESOURA'
com = randint(1,3)
if com == 1:
    comesc = 'PEDRA'
elif com == 2:
    comesc = 'PAPEL'
elif com == 3:
    comesc = 'TESOURA'

sleep(0.5)
print('\33[34m-=\33[m'*13)
print('\33[1;35mJO...',end='')
sleep(0.7)
print('\33[1;33mKEN...\33[m',end='')
sleep(0.7)
print('\33[1;;32mPO!!!!!!\33[m')
sleep(0.5)
print('\33[34m-=\33[m'*13)

if jogador == com:
    print('\33[1;34mPlayer\33[m {} \33[31mx\33[m {} \33[1;34mComputer\33[m'.format(jogesc , comesc))
    print('\33[33;4mEmpate!\33[m')
elif jogador == 1 and com == 2 or jogador == 2 and com == 3 or jogador == 3 and com == 1:
    print('\33[1;34mPlayer\33[m {} \33[31mx\33[m {} \33[1;34mComputer\33[m'.format(jogesc, comesc))
    print('Você \33[4;31mPERDEU!\33[m')
elif jogador == 1 and com == 3 or jogador == 2 and com == 1 or jogador == 3 and com == 2:
    print('\33[1;34mPlayer\33[m {} \33[31mx\33[m {} \33[1;34mComputer\33[m'.format(jogesc, comesc))
    print('Você \33[4;32mVENCEU!')
else:
    print('\33[31mJOGADA INVALIDA!!!\33[m')
