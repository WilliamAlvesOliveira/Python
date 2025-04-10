print('     Tabela do Brasileirão')
print('Última atualização dia 02/10/21')
clubes= ('Botafogo','Palmeiras','Fortaleza','Flamengo','São Paulo','Bahia','Internacional',
         'Cruzeiro','Vasco da Gama','Atlético MG','Bragantino','Juvehtude','Grêmio',
         'Crisciúma','Atlético PR','EC Vitória','Corinthians','Fluminense',
         'Cuiabá','Atlético GO')
while True:
    op = int(input('''\33[31m[1]\33[mMostrar times do \33[34mG4\33[m
\33[31m[2]\33[mMostrar times da \33[31mzona de rebaixamento
\33[31m[3]\33[mMostrar os times do campeonato
\33[31m[4]\33[mProcurar a classificação do seu time
\33[31m[5]Sair\33[m
Selecione uma opção: '''))
    if op == 1:
        print(clubes[:4])
    elif op == 2:
        print(clubes[-4:])
    elif op == 3:
        print(sorted(clubes))
    elif op == 4:
        search = str(input('Qual time você deseja saber a classificação: '))
        if search not in clubes:
            print(f'O time {search} não foi encontrado!')
        else:
            print(f'{search} está na {clubes.index(search)+1}ª posiçãp')
    elif op == 5:
        break
    else:
        print('\33[31m0Opção invalida!\33[m')
print('Fim do programa')
