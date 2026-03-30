n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 < n2:
    m = n1
    M = n2
else:
    m = n2
    M = n1
n3 = int(input('Digite o terceiro valor: '))
if n3 < m:
    m = n3
if n3 > M:
    M = n3
print('O menor número foi ',m)
print('O maior número foi ',M)