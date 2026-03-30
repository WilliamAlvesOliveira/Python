galera = list()
dados = []
for c in range(0,4):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
print('Maiores de idade')
for p in galera:
    if p[1] >= 18:
        print(f'Nome: {p[0]}, Idade: {p[1]}')
print('Menores de idade')
for p in galera:
    if p[1] < 18:
        print(f'Nome: {p[0]}, Idade: {p[1]}')
print('FIM DA LISTAGEM')

