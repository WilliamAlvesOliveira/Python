ficha = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2)/ 2
    ficha.append([nome, [nota1, nota2],média])
    resposta = str(input('Deseja continuar?: ')).strip().lower()
    if resposta in 'n':
        break
print('-'*39)
print(f'{"No.":<4}){"NOME":<10}{"MÉDIA":>8}')
print('-'*36)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opç = int(input('Mostrar as notas de qual aluno? [999 interrompe]: '))
    if opç == 999:
        print('FINALISANDO...')
        break
    if opç <= len(ficha)-1:
        print(f'Notas de {ficha[opç][0]} são {ficha[opç][1]}')
print('Volte sempre')
