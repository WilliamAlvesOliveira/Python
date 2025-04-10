#faça um programa que tenha uma função que receba três parâmetros:
# início, fim e passo e realize a contagem. seu programa tem que realizar três
# contagens atávez da função criada.
#A) de 1 até 10. de 1 em 1 B) de 10 até 0 de 2 em 2 C)uma contagem presonalizada.

from time import sleep

def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end='  ')
            sleep(0.2)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end='  ')
            sleep(0.2)
            cont -= p
        print('FIM')


#programa principal
contador(1,10,1)
contador(10,0,2)
contador(int(input('inicio: ')),int(input('fim: ')),int(input('salto: ')))