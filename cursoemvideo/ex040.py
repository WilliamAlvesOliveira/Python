nome = str(input('Nome do aluno: '))
n1 = float(input('Qual foi a 1º nota do/a {}: '.format(nome)))
n2 = float(input('Qual foi a 2º nota do {}: '.format(nome)))
média = (n1 + n2)/ 2
if média < 5:
    print('Média: \33[31m{:.1f}\33[m'.format(média))
    print('{} está \33[1;31mREPROVADO!(a)'.format(nome))
elif média >= 5 and média < 7:
    print('Média: \33[33m{:.1f}\33[m'.format(média))
    print('{} está de \33[1;33mRECUPERAÇÃO'.format(nome))
elif média >= 7 and média <+ 10:
    print('Média: \33[32m{:.1f}\33[m'.format(média))
    print('{} está \33[1;32mAPROVADO(a)!'.format(nome))
else:
    print('\33[31mERRO!!\33[m')
