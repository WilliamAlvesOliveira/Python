#crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitas em cada partida.
# no final isso tudo sera guardado em um dicionario incluindo o total de gols feitos durante o campeonato
jogador = {}
gols = []
total_gols = 0
#entrada
jogador['nome'] =  str(input('Nome do Jogador: '))
jogador['jogos'] = int(input(f'Quantas jogos o {jogador["nome"]} jogou: '))
for jogos in range(1, jogador['jogos']+1):
    gol = (int(input(f'Quantos gols o {jogador['nome']} fez no {jogos}º jogo: ')))
    gols.append(gol)
    total_gols += gol
jogador['gols'] = gols
jogador['total'] = total_gols
jogador['aproveitamento'] = total_gols / jogador['jogos']

print('-='*40)
print(jogador)
print('-='*40)

#sa[ida
print(f'{'Nome':<15}|{'Q.Jogos':>10} |{'Gols':>8}| {'aproveitamento':>15}|')
print(f'{jogador["nome"]:<15}|{jogador["jogos"]:>11}|'
      f'{jogador["total"]:>8}|{jogador["aproveitamento"]:>16.2f}|')
print('-='*40)
