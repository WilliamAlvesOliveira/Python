def fatorial (n):
    c = 1
    for c in range(c, n+1):
        f *= c
    return f


num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é `{fat}')