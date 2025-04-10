#aprimore o ex anterior mostrando no final: A a soma de todos os valores pares
#B as soma dos valores da terceira coluna, C o maior valor da segunda linhalinha1 = []
matriz = [[],[],[]]
totpar = totcol = l2m = cont= 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(int(input(f'Digite o valor da linha {l} na posição {c}: ')))

print('-'*20)
print('matriz')
print('-'*20)

for pos, l in enumerate(matriz):
    totcol += l[2]
    for v in l:
        print(f'{v:^5}', end='')
        if v %2 == 0:
            totpar += v
        if  pos == 1:
             if v > l2m:
                 l2m = v
    print()

print('-'*20)
print(f'O total dos valores pares é de {totpar}')
print(f'O valor total da coluna 3 é {totcol}')
print(f'O valor total da linha 2 é {l2m}')
