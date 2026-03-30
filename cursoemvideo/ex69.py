#Crue um pograma que leia a idade e o sexo de  varias pessoas  a cada pessoa
#p programa devera perguntar se o usuario que ou não cadasrar mais pessoas
#no fial mostre. quanras pessoas maiores de 18 anos, wusnt homens, wusnt mul 20 -
MI = H = MMI = 0
while True:
    print('Cadastro de pessoas')
    print('-'*30)
    nome = str(input('Digite o neme: '))
    sexo = str(input('Qual é o sexo [M/F]: ')).upper().strip()[0]
    while sexo not in 'MF':
        print('\33[31mOpção invalida!\33[m')
        sexo = str(input('Qual é o sexo [H,M]: ')).upper().strip()[0]
    if sexo == 'M':
        H += 1
    idade = int(input('Quall é a idade: '))
    if idade >= 18:
        MI += 1
    if sexo == 'F' and idade > 20:
        MMI += 1
    op = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    while op not in 'SN':
        print('\33[31mOpção invalida!\33[m')
        op = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    print('-'*30)
    if op == 'N':
        break
print(f'Pessoas maiores de idade: {MI}')
print(f'Números de Homens cadastrados: {H}')
print(f'Números de mulheres maiores de 20 anos: {MMI}')
