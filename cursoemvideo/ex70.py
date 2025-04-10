#que leia o noe e o preço de varios produtos deve perguntar se deseja continuar
#e mostre quaal o total gasto, quantos produtos mais de 1000
# , e o nome do produto mais varato
VT = PC = 0
PB = ''
print('='*30)
print('LOJA BARATAS')
print('='*30)
while True:
    nome = str(input('Nome do produto: '))
    v = float(input(f'Qual o valor do {nome}: '))
    if VT == 0 or v < vPB:
        PB = nome
        vPB = v
    if v > 1000:
        PC += 1
    op = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    while op not in 'SN':
        print('\33[31mOpção invalida\33[m')
        op = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    VT += v
    print('-'*30)
    if op == 'N':
        break
print(f'O valor total foi de: {VT:.2f} R$')
print(f'Número de produtos que custam mais de 1.000 R$: {PC}')
print(f'O produto mais barato foi: {PB}')