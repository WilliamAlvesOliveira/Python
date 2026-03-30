time = []

# Cadastro
print(f'{"Cadastro de Jogadores":^57}')
while True:
    print('=' * 57)
    jogador = dict()
    jogador['nome'] = str(input('Nome: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))

    gols = []
    for jogos in range(jogador['partidas']):
        gols.append(int(input(f'Quantos gols {jogador["nome"]} fez no {jogos + 1}º jogo: ')))

    jogador['gols'] = gols
    jogador['total gols'] = sum(gols)
    jogador['média'] = jogador['total gols'] / jogador['partidas'] if jogador['partidas'] > 0 else 0

    time.append(jogador.copy())

    # Opção de novo cadastro
    while True:
        opcao = str(input('Deseja cadastrar outro jogador? [S/N]: ')).strip().lower()
        if opcao in ('s', 'n'):
            break
        print('Opção inválida!')

    if opcao == 'n':
        break

# Saída de Dados
print('=' * 57)
print(f'{"nº":<2} | {"Nome":<15} | {"Q.Jogos":>10} | {"Gols":>8} | {"Aproveitamento":>15} |')
print('-' * 57)
for pos, j in enumerate(time):
    print(f'{pos:<2} | {j["nome"]:<15} | {j["partidas"]:>10} | {j["total gols"]:>8} | {j["média"]:>15.2f} |')

# Opção de Visualização de Gols
while True:
    # Validação
    while True:
        opcao = str(input(f'{" Deseja consultar gols? [S/N]: ":=>57}')).strip().lower()
        if opcao in ('s', 'n'):
            if opcao == 's':
                while True:
                    numero = int(input('Qual o número do jogador: '))
                    if 0 <= numero < len(time):
                        print(f'{time[numero]["nome"]} jogou {time[numero]["partidas"]} {"partida" if time[numero]["partidas"] == 1 else "partidas"}')
                        for j, g in enumerate(time[numero]['gols']):
                            print(f'Fez {g} {"gol" if g == 1 else "gols"} na {j + 1}º partida')
                        break
                    else:
                        print('Jogador não encontrado!')
            break
        print('Opção inválida!')
    if opcao == 'n':
        break

# Finalizando Programa
print(f'{"PROGRAMA ENCERRADO!":^57}')
