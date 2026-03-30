#Faça um orograma que leia nome e peso de varias pessoas e quarde tudo em uma lista
# no final mostre A quantas pessoas foram cadastradas, B uma listagem com as pessoas pesadas
#C uma listagem com as pessoas mais leves " pessoas pesadas acima de 100
dados = []
cadastros = []
maior = menor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(cadastros) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    cadastros.append(dados[:])
    dados.clear()

    op = str(input('Deseja continuar?\33[31m[S/N]\33[m: ')).strip().lower()
    while op not in 'sn':
        print('\33[31mOpção invalida!\33[m')
        op = str(input('Deseja continuar?\33[31m[S/N]\33[m: ')).strip().lower()
    if op == 'n':
        break

print('-'*50)
print('CADASTRADOS')
print(f'Número de cadastrados:  {len(cadastros)}')
for p in cadastros:
    print(f'Nome: {p[0]}, Peso: {p[1]}')
print('_'*50)
print('Pessoas mais pesadas')
for c in cadastros:
    if c[1] == maior:
        print(f'Nome: {c[0]}, Peso: {c[1]}')
print('_'*50)
print('Pessoas mais leves')
for c in cadastros:
    if c[1] == menor:
        print(f'Nome: {c[0]}, Peso: {c[1]}')
print('_'*50)
print('FIM DO PROGRAMA')
