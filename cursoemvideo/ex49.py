#refaça o ex 09 mostrando um numero que o usuario vai escolher, utilizando o for
q = int(input('A tabuada de qual número voce deseja ver: '))
for c in range(1,11):
    print('{} x {} = {}'.format(q,c,q*c))