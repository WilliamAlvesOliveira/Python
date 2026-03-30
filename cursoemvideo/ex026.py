frase = str(input('Digite uma frase: ')).strip()
print('Quantas vezes aparece a letra A: ',frase.lower().count('a'))
print('A primeira letra A apareceu na posição: ',frase.lower().find('a')+1)
print('A ultima letra A apareceu na posição: ',frase.lower().rfind('a')+1)
