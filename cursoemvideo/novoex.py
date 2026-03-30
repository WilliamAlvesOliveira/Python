totalidade = mulheresjovens = ncadastos = 0
nomemaisvelho = 'Nenhum'
for c in range (0,4):
    print('CADASTRO')
    print('-'*10)
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    totalidade = totalidade + idade
    sexo = str(input('SEXO [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        print('\33[31mOpção incalida!\33[m')
        sexo = str(input('SEXO [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        if nomemaisvelho == 'Nenhum':
            nomemaisvelho = nome
            idademaisvelho = idade
        else:
            if idademaisvelho < idade:
                nomemaisvelho = nome
    if sexo =='F':
        if idade < 21:
            mulheresjovens = mulheresjovens + 1
    ncadastos += 1
media = totalidade  / ncadastos
print(f'Média de idade das pessoas cadastradas: {media:1f}')
print(f'O homem mais velho cadastrado foi: {nomemaisvelho}')
print(f'Quantidade de mulheres com menos de 21 anos: {mulheresjovens}')
