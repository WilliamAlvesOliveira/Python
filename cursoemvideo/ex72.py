op = 'S'
num = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez',
       'Onze','Dpze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito',
       'Dezenove','Vinte')
while True:
    n = int(input('Selecione um número de 0 a 20 para ver escrito por extenso: '))
    if n <0 or n> 20:
        print('\33[31mOpção invalida!\33[m')
    print(f'Vpcê dogitou o númrto: \33[34m{num[n]}\33[m')
    while True:
        op = str(input('Deseja continuar [S/N]: ')).strip().upper()
        if op == 'S'or op == 'N':
            break
        else:
            print('\33[31mOpção invalida!\33[m')
    if op == 'N':
        break
print('Fim do programa')
