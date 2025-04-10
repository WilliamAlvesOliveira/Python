#faça um programa que tenha uma lista chamada números e duas funções
# chamada sorteio() e somapar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vami mostrar a soma entre todos os valores pares sorteados
# pela função anterior.
from os import lseek
from random import randint

numeros = list()

def sorteio(numeros):
    for c in range(0,5):
       numeros .append(randint(0,10))
    print(f'Os números sorteados foram {numeros}')

def somapar(numeros):
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'A soma dos valores pares é {soma}')


sorteio(numeros)
somapar(numeros)
