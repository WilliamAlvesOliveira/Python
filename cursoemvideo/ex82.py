#crie um programa que vai ler vários números e coloque em uma lista
#Depois crie duas listas extras que vão conter os números pares e impares respectivamente
#no final mostre o valor das três listas geradas
A = []
B = []
C = []
while True:
    A.append(int(input('Adicione um número a lista: ')))
    op = str(input('Deseja adicionar outro número?\33[31m[S?N]\33[m:'))
    while op not in 'sn':
        print('\33[31mOpção invalida~1\33[m')
        op = str(input('Deseja adicionar outro número a lista?\33[31m[S/N]\33[m:'))
    if op == 'n':
        break
for c in A:
    if c % 2 == 0:
        B.append(c)
    else:
        C.append(c)
print(f'Lista completa {A}')
print(f'Lista com os números pares {B}')
print(f'Lista com os números impares {C}')
