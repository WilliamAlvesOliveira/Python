#crie um programa que o úsuario possa digitar 5 valores numéricos e cadastre em uma lista
# ponha eke na posição correta sem usar o sort
#no final mostre a lista ordenada na tela
lista = []
for c in range(0,5):
    n = int(input('Digite um valor para ser adicionado a lista: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('número adicionado a lista' if c == 0 else'Número adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print('número adicionado no inicio da lista' if pos== 0 else f'Número adicionado na posição {pos}')
                break
            pos += 1
print('-'*30)
print(lista)
print('\33[04mFIM DO PROGRAMA!\33[m')
