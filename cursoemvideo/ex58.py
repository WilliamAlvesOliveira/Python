#3melhore o jogo do des 28 , so que agora o jogador vai tentar adivinhar o númeroo
#até acertar mstrano quantas tenativas foram necessárias
from random import randint
X = randint(0,100)
r = (int(input('Tente adivinhar o número que eu pensei(\33[35m0\33[m à \33[36m100\33[m): ')))
t = 1
while r != X:
   if r > X:
       r = int(input('Você \33[31mERROU!\33[m É \33[35mMenos!\33[m Temte novamente: '))
       t = t + 1
   else:
       r = int(input('Você \33[31mERROU!\33[m É \33[36mMais!\33[m Tente novamente: '))
       t = t + 1
print('Parabéns!!! Você \33[32mACERTTOU\33[m na \33[34m{}\33[mª tentativa.'.format(t))
