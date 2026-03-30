#crie um programa onde o usuário cadastre 7 pessoase cadastre em uma listq única que
#mantenha separados os valores pares e impares. no final mostre os valores pares e impares
# na ordem crescente
numeros = []
for c in range(1,8):
    numeros.append(int(input('Digite p[x] valor: ')))
print('_'*50)
print(f'Valores: {numeros}')
numeros.sort()
print('Números pares digitados')
for c in numeros:
    if c % 2 == 0:
        print(c, end=' ')
print()
print('Números impares digitados')
for c in numeros:
    if c % 2 == 1:
        print(c, end=' ')
