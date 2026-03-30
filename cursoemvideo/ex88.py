#faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai
#perguntar quantos jogos serão gerados e vai sortear os números entre 1 e 60 para cada jogo
#cadastrando tudo em uma lista composta.
from random import randint

palpites = list()
numeros = []
njogos = int(input('Wuantos palpites você deseja receber? '))

for j in range(0,njogos):
    for n in range(0, 6):
        num = randint(0, 60)
        while True:
            if num not in numeros:
                numeros.append(num)
                break
            else:
                num = randint(0,60)
    numeros.sort()
    palpites.append(numeros[:])
    numeros.clear()

for pos,  p in enumerate(palpites):
    print(f'Jogo {pos +1}: {p}')