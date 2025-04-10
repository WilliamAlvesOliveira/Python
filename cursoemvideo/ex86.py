#crie um programa que cria uma matriz 3x3 e preencha os valores lidos pelo teclado.
# e no final mostre tudo com a formatação correta
matriz = [[],[],[]]

for l in range(1,4):
    for c in range(1,4):
        matriz[l-1].append(int(input(f'Digite o valor da linha {l} na posição {c}: ')))

print('matriz')
print('-'*20)
for c in matriz:
    for l in c:
        print(f'{l:^5}',end='')
    print()
