#faça um programa que leia o sexo  de uma pessoa mas so aceite os valores h ou map
#caso errado peça  a digitação novamente até estar correto
s = str(input('Digite seu sexo \33[31m[M/F]\33[m: ')).strip().upper()
while s not in 'MF':
    print('\33[31mOpção invalida!\33[m')
    s = str(input('Digite o seu sexo \33[31m[H/M]\33[m: ')).strip().upper()
print('O seu sexo é masculino' if s == 'M' else 'O seu sexo é feminino')
