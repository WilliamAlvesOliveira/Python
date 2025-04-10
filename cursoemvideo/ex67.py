#faça um programa que mostre a tabuada de varios npumeros de cada vez para
#caada valor digitado. o programa para quando o valor digitado for negativo
while True:
    n = int(input('Quer ver a tabuada de qual número: '))
    if n < 0:
        break
    for c in range (1,11):
        print(f'{n} x {c} = {n*c}')
print('Programa encerrado!')
