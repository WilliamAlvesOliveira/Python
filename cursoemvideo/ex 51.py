#desenolva um programa que leia o primeiro termo e a razão de uma progressão
#aritimética e no final mostre os 10 primeiros termos desta progreção
print('='*30)
print('{}10 TERMOS DE UMA PA'.format(' '*5))
print('='*30)
t = int(input('Primeiro termo: '))
r= int(input('Razão: '))
for c in range(1, 11):
    print(t,end= ' ')
    t = t + r
print('Fim.')
