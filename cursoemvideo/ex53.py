#crie um programa que leia uma frase qualquer e diga se ela pe um palindrome
#desconsiderando os espaços
f = str(input('DIgite uma frase: ')).strip().upper()
fs= f.split()
fj = ''.join(fs)
fr = ''
x = len(fj)
for c in range(1, x+1):
    fr = fr + fj[x-c]
if fr == fj:
    print('A frase {} é um palindromo\n{}'.format(f,fr))
else:
    print('A frase {} não é um palindromo!'.format(f))
