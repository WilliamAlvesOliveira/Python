nome = input('Digite o nome do aluno: ')
n1 = float(input('Qual foi a 1ª nota do/da {}: '.format(nome)))
n2 = float(input('Qual foi a 2ª nota do/da {}: '.format(nome)))
media  = (n1 + n2)/2
print('A média do/da {} é {:.1f}'.format(nome,media))