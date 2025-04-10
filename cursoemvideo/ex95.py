#crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitas em cada partida.
# no final isso tudo sera guardado em um dicionario incluindo o total de gols feitos durante o campepnaro

#validação de números inteiros
def validação(mensagem):
    while True:
        try:
            entrada = int(input(mensagem))
            return entrada
        except ValueError:
            print('\33[31mErro!\33[m por favor digite apenas números.')


#ptograna principal
time = []
#cadastro
print(f'{"Cadastro de Jogadores":^60}')
while True:
    print('='*60)
    jogador = dict()
    jogador['nome'] = str(input('Nome: '))
    jogador['partidas'] = validação(f'Quantas partidas {jogador["nome"]} jogou: ')

    gols = list()
    for jogos in range(0,jogador['partidas']):
        gols.append(validação(f'   Quantos gols {jogador["nome"]} fez no {jogos+1}º jogo: '))

    jogador['gols'] = gols[:]
    jogador['total gols'] = sum(jogador['gols'])

    if jogador['partidas'] > 0:
        jogador['média'] = jogador['total gols'] / jogador['partidas']
    else:
        jogador['total gols'] = 0
        jogador['média'] = 0


    time.append(jogador.copy())

    #opção de novo cadastro
    while True:
        opção = str(input('Deseja cadastrar outro jogador? [S/N]: ')).strip().lower()
        if opção in ('s','n'):
            break
        print('\33[31mOpção inválida!\33[m')
    if opção == 'n':
        break

#saida
print('='*60)
print(f'{"ind. "}|{'Nome':<15}|{'Q.Jogos':>10} |{'Gols':>8}| {'aproveitamento':>15}|')
print('-'*60)
for pos, j in enumerate(time):
    print(f'{pos:>4} |{j["nome"]:<15}|{j["partidas"]:>11}|'
          f'{j["total gols"]:>8}|{j["média"]:>16.2f}|')

#opção de visualização de gols
while True:

    #validação
    while True:
        opção = str(input((f'{" Deseja consultar gols? [S/N]: ":=>57}'))).strip().lower()
        if opção in ('s','n'):
            #seleção de jogador
            if opção == 's':
                while True:
                    número = validação('Qual o indice do jogador: ')
                    if número < 0 or número > len(time)- 1:
                        print('Jogador \33[31mnão encontrado!\33[m')
                    else:
                        print(f'{time[número]["nome"]} jogou {time[número]["partidas"]} '
                              f'{"partida" if time[número]["partidas"] == 1 else "partidas"}')
                        for j, g in enumerate(time[número]['gols']):
                            print(f'   fez {g} {"gol" if g == 1 else "gols"} na {j+1}º partida')
                    break
            break
        print('\33[31mOpção inválida!\33[m')
    if opção == 'n':
        break

#finalizando programa
print()
print(f'{"\33[04mPROGRAMA ENCERRADO!\33[m":^60}')
print()
print('='*60)
