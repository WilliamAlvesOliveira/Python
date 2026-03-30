from random import randint
numeros = (randint(0,10), randint(0,10),
     randint(0,10), randint(0,10),
     randint(0,10))
print('Os números sorteados foram:')
for n in numeros:
    print(f'{n} ',end='')
print(f'\nO menor número foi {max(numeros)}')
print(f'E o maior número foi {min(numeros)}')
