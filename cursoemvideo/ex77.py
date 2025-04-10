#escreva um programa que tenha uma tupla com várias palavres sem acentos. Depois disso
#você deve mostrar para cada palavra, quais são as suas vogais.
palavras = ('Iron Maiden', 'Ramones','Black Sabbath', 'Deep purple', 'Led Zeppelin', 'Saurom',
            'Mago de Oz, Celtian', 'Megadeth', 'Rage Against the Machine')
print(palavras)
for p in palavras:
     print(f'\nNa palavra \33[34m{p}\33[m temos as vogais: ',end='')
     for letra in p:
         if letra.lower() in 'aeiou':
             print(letra.lower(),end=' ')


