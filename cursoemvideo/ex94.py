#crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No fina, mostre: A) quantas pessoas foram cadastradas
# B) média de idade do grupo
# C) Uma lista com todas as mulheres
# D) Uma lista com todas as pessoas acima da média.

cadastros = list()
pessoa = {}
total_idade = 0
homens = list()
mulheres= list()
acima_media = list()
#cadastro
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input(f'Qual é o sexo de {pessoa["nome"]}?[M/F]: ')).strip().lower()
        if pessoa['sexo'] in ('m','f'):
            break
        print('Opção invalida.')
    pessoa['idade'] = int(input(f'Quantos anos {"a"if pessoa["sexo"] == "f" 
    else "o"} {pessoa['nome']} tem: '))
    while True:
        opção = str(input('Deseja fazer um novo cadastro?[S/N]: ')).strip().lower()
        if opção in ('s' , 'n'):
            break
        print('Opção invalida.')
    cadastros.append(pessoa.copy())
    if opção == 'n':
        break
#coleta de dados
total_cadastros = len(cadastros)
for p in cadastros:
    total_idade += p['idade']
    if p['sexo'] == 'm':
        homens.append(p['nome'])
    else:
        mulheres.append(p['nome'])
media = total_idade / total_cadastros
for p in cadastros:
    if p['idade']> media:
        acima_media.append(p)


#saída de dados
print(cadastros)
print('='*30)
print(f'Nº de pessoas cadastradas: {total_cadastros}')
print(f'A média de idade das pessoas cadastradas foi de: {media}')
print(f'Listagem de Homens cadastrados:\n{homens}')
print(f'Listagem de Mulheres cadastradas:\n{mulheres}')
print(f'Pessoas com idade acima da média:\n{acima_media}')
