#Faça um programa que tenha uma funçãl chamada maior() que receba vários parâmetros
# com valores inteiros. Seu programa deve analisar todos os valores
# e dizer qual deles é o maior
from time import sleep

def maior (*num):
    mai =  0
    quant = len(num)
    print('Analizando valores...')
    sleep(0.5)
    print (num)
    for n in num:
        print(n,end=' ')
        if n > mai:
            mai = n
    print(f'Ao todo fora analizados {quant} números')
    print(f'E o maior número analizado foi {mai}')


maior(1,4,1,3,1,3,4,5,6,4)
maior()