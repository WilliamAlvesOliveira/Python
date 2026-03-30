#faça um programa que tenha a função ficha. que receba dois parâmetros
# opcionais: o nomr de um jogador e quantos gols ele marcou..
# O programa deve ser capaz de mostrar a ficha do jogador. mesmo que algum dado não
# tenha sido informado corretamente
from unicodedata import numeric


def ficha (jog='Desconhecido', gol = 0):
   print(f'O jogador {jog} marcou {gol} gols')


n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
   ficha(gol = g)
else:
    ficha(n, g)
