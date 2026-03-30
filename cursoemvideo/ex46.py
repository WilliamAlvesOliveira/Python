#faça um programa que mostre uma comtagem regressiva para o estouro de fogos
#indo de 10 até 0 com uma pausa de 1 segundo entre eles
from time import sleep
from random import randint
cor = ['\33[31m','\33[32m','\33[33m','\33[34m','\33[35m','\33[36m','\33[37m']
print('\33[34mContagem Regrassiva para o Reveilon\33[m')
for c in range(10,0,-1):
    x = randint(0,6)
    print('{}{}'.format(cor[x],c ), end=' ')
    sleep(1)
print('\33[31mfogos\33[m')
