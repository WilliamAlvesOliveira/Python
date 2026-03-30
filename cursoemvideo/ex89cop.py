students = []
record = []

print('Cadastro de Alunos')
while True:
    print('='*36)
    record.append(str(input('Nome: ')))
    for i in range(1, 3):
        record.append(float(input(f'Nota {i}: ')))
    record.append(sum(record[1:3])/2)  # Calculando a média
    students.append(record[:])
    record.clear()

    while True:
        option = str(input('Deseja fazer outro cadastro? [S/N]: ')).strip().lower()
        if option in ['s', 'n']:
            break
        print('Opção inválida!')
    if option == 'n':
        break

print('='*36)
print(f'{"Boletim":^30}')
print(f'{"Nome":20}Média')
print('-'*36)
for student in students:
    print(f'{student[0]:20}{student[3]}')
print('='*36)

while True:
    option = str(input('Deseja consultar notas? [S/N]: ')).strip().lower()
    if option in ['s', 'n']:
        if option == 'n':
            break
        search_name = str(input('Nome do Aluno: '))
        found = False
        for student in students:
            if student[0] == search_name:
                print(f'{"Nota 1":10}{"Nota 2"}')
                print(f'{student[1]:<10}{student[2]}')
                found = True
        if not found:
            print('Aluno não encontrado')
    else:
        print('Opção inválida!')
print('='*36)
print('FIM DO PROGRAMA')
print