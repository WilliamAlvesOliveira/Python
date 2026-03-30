#crie um programa que vai ler valores numéricos e colocar em uma lista
#e depois disso mostre A: quantos números foram digitados
#B a lista de valores ordenada de forma decrescente
#Cse o valor 5 for digitado ou não na lista
from itertools import count
cont = 0
lista = []
while True:
    lista.append(int(input('Adicione um número a lista: ')))
    op = str(input('Deseja continuar?\33[31m[S/N]\33[m:')).strip().lower()
    while op not in 'sn':
        print('\33[31mopção inválida!\33[m:')
        op = str(input('Deseja continuar?\33[31m[S/N]\33[m:')).strip().lower()
    if op == 'n':
        break
lista.sort(reverse = True)
print('-'*30)
print(f'você digitou {len(lista)} elementos')
print(f'Os elementos em ordem decrescente são {lista}')
if 5 not in lista:
    print('Não há número 5 na lista')
else:
    print('O valor 5 faz parte da lista')
    for c in range (0, len(lista)):
        if lista[c] == 5:
            cont += 1
        print(f'Quantidade de número 5 na lista {cont}')
