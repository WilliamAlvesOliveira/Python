#crie um programa qu leia varios numeroos e no fim mostre a media qul o maior e o menor
op = 'S'
Mn = mn = s = n = q = 0
while op not in 'N':
    n = int(input('Digite um número: '))
    q += 1
    if q == 1:
        Mn = mn = n
    s += n
    if n > Mn:
        Mn = n
    elif n < mn:
        mn = n
    op = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    while op not in 'SN':
        op = str(input('\33[31mOpção invalida\33[m\nDeseja continuar? [S/N]: ')).upper().strip()[0]
print('Quantidade de números digitados: {}\nMédia entre eles foi: {}.'.format(q,s/q))
print('O maior número foi {}\nO menor número foi {}'.format(Mn,mn))
