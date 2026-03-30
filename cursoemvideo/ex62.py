# melhore o ex 61  adicionando  uma oção que peça para o usuário quantos valores mais
#o usuario deseja ver
print('='*30)
print('{}TERMOS DE UMA PA'.format(' '*6))
print('='*30)
c = 0
t = int(input('Primeiro termo: '))
r= int(input('Razão: '))
q = int(input('Quantos valores você deseja? '))
qt = 0
while q != 0:
    while c != q:
        print(t, end=' ')
        t = t + r
        c = c + 1
        qt += 1
    c = 0
    q = int(input('\nQuantos termos mais você deseja ver: '))
print('A progressão foi finalizada exibindo {} termos no total.'.format(qt))
