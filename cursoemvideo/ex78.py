#faça um programa que leia 5 valores numéricos e guarde em uma lista
#no final mostre a lista e qual foi o maior e o menor valor e suas respectivas posições
lista = []
M = m = 0
for  c in range(0,5):
    lista.append(int(input(f'Digite um número na posição {c}: ')))
    if c == 0:
        M = m = lista[c]
    else:
        if lista[c] < m:
            m = lista[c]
        elif lista[c] > M:
            M = lista[c]
print('-'*30)
print('Você digitou os valores',lista)
if lista.count(m) == 1:
    print(f'O menor número digitado foi {m} na posição: {lista.index(min(lista))}')
else:
    print(f'O menor número digitado foi {m} nas posições: ',end='')
    for i, v in enumerate(lista):
            if lista[i] == m:
                print(f'{i} ',end='')
    print()
if lista.count(M) == 1:
    print(f'E o maior número foi {M} na posição {lista.index(max(lista))}')
else:
    print(f'E o maior número digitado foi {M} nas posições: ',end='')
    for i, v in enumerate(lista):
        if lista[i] == M:
            print(i,end=' ')

