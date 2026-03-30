#Crie um programa que leia o nome e 2 notas de vários alunos, guarde tudo em uma lista
# composta. No final mostre um boletim com nome e a média de cada um
# e permita que o usuário possa mostrar as notas de cada aluno idividualmente
alunos = []
cadastro = []

print('Cadastro de Alunos')
while True:
    print('='*36)
    cadastro.append(str(input('Nome: ')))
    for n in range(1,3):
        cadastro.append(float(input(f'Nota {n}: ')))
    cadastro.append((cadastro[1]+cadastro[2])/2)
    alunos.append(cadastro[:])
    cadastro.clear()
    op = str(input('Deseja fazer outro cadastro?\33[31m[S/N]\33[m: ')).strip().lower()
    while op != 's':
        if op == 'n':
            break
        print('\33[31mOpção invalida!\33[m')
        op = str(input('Deseja fazer outro cadastro?\33[31m[S/N]\33[m: ')).strip().lower()
    if op == 'n':
        break
print('='*36)
print(f'{"Boletim":^30}')
print(f'{"Nome":20}Média')
print('-'*36)
for a in alunos:
    print(f'{a[0]:20}{a[3]}')
print('='*36)
op = str(input('Deseja consultar notas?\33[31m[S/N]\33[m: '))
while op != 'n':
    if op == 's':
        val = 0
        print('='*36)
        search = str(input('Nome do Aluno: '))
        for a in alunos:
            for n in a:
                if search == n:
                    print('='*36)
                    print(n)
                    print(f'{"Nota 1":10}{"Nota 2"}')
                    print(f'{a[1]:}{a[2]:10}')
                    val = 1
        if val == 0:
            print('\33[31mAluno não encontrado\33[m')
        op = str(input('Deseja consultar notas?\33[31m[S/N]\33[m:')).strip().lower()
    while op != 's':
        if op == 'n':
            break
        print('\33[31mOpção incalida!\33[m')
        op = str(input('Deseja consultar notas?\33[31m[S/N]\33[m:'))
print('='*36)
print('FIM DO PROGRAMA')
print('='*36)
