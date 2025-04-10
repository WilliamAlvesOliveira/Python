jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Wuantas jogos {jogador["nome"]} jogou?: '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c}: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} Jogou {len(jogador["gols"])} partidas.')
print('-='*30)
for i, v in enumerate(jogador['gols']):
    print(f'   => na partida {i}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')
