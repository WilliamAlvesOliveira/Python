#que simule um caixa eletronico pergunte o vslor e mostre qquantas cedilas
# de cada valor serra entregue cedulas de 50 20 10 1
n1 = n2 = n3 =n4 = sv = v = 0
print('-'*30)
print('{:^30}'.format('BANCO BUFUNFA'))
print('-'*30)
valor = int(input('Qual e o valor que você deseja sacar: '))
while v != valor:
    sv = v + 50
    if sv <= valor:
        v += 50
        n1 += 1
    else:
        sv = v + 20
        if sv <= valor:
            v += 20
            n2 += 1
        else:
            sw = v + 10
            if sw <= valor:
                v += 10
                n3 += 1
            else:
                sw = v + 1
                if sw <= valor:
                    v += 1
                    n4 += 1
print(f'Valor sacado: {valor} R$')
print(f'''Quantidade de cédulas:
{n1} notas de 50 R$
{n2} notas de 20 R$
{n3} notas de 10 R$
{n4} notas de 1 R$''')