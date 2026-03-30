# Crie um programa em que 4 jogadores joguem um dado e tenham resultados aleatórios.
# guarde esses resultados em um dicíonário. No final, coloque esses resultados em ordem,
# sabendo que o vencedor tirou o maior número no dado.
from random import randint
from operator import itemgetter
from time import sleep

player = {}
#declarando jogadores e resultados
for cont in range(1,5):
    player[f'Jogador{cont}'] = randint(1,6)
ranking = list()

#exibição dos resultados
print('Valores sorteados')
for cont in range(1,5):
    print(f'Jogador{cont} tirou {player[f"Jogador{cont}"]} no dado')
    sleep(0.7)
print('-'*30)

#definindo colocaçõpes
print('Ranking')
ranking = sorted(player.items(), key=itemgetter(1), reverse=True)
for indice, jogador in enumerate(ranking):
    print(f'{indice+1}º lugar {jogador[0]} com {jogador[1]}')
