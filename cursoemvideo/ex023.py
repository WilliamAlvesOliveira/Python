n = int(input('Digite um número: '))
print('Analisando o número ',n)
print('O número {} tem\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(n, n//1%10, n//10%10, n//100%10,n//1000%10))