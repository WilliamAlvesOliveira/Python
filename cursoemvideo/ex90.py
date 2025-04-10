#faça um programa que leio o nome e a média de um aluno, guardando também a situação
# em um dicionário. No final mostre o conteúdo da estrutura toda.

#entrada de dados
alunos = {}
alunos['nome'] = str(input('Nome do Aluno: '))
alunos['média'] = float(input(f'Qual é a média do {alunos["nome"]}: '))

# Verificação da Média
while not 0 <= alunos['média'] <= 10:
    print("Média inválida. Por favor, insira um valor entre 0 e 10.")
    alunos['média'] = float(input(f'Qual é a média do {alunos["nome"]}: '))

# Determinação da Situação
if alunos['média'] >= 7.5:
    alunos['situação'] = 'Aprovado'
elif alunos['média'] >= 5:
    alunos['situação'] = 'Recuperação'
else:
    alunos['situação'] = 'Reprovado'

#saída
print()
print('='*36)
print(f'{"Nome":<15}{"Média":<10}{"Situação"}')
print('-'*36)
print(f'{alunos["nome"]:<15}',end='')
print(f'{alunos["média"]:<10.1f}',end='')
if alunos['média'] >= 7.5:
    print('\33[32mAprovado\33[m')
elif alunos['média'] >= 5:
    print('\33[33mRecuperação\33[m')
else:
    print('\33[31mReprovado\33[m')
print('='*36)
