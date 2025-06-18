n = int(input('Digite um número: '))
print('O antecesor de {} é {}\n e o sucessor é {}'.format(n, n-1, n+1))

#forma mais moderna com fstrings
print(f'O antecessor de {n} é {n - 1}\ne o sucessor é {n + 1}')