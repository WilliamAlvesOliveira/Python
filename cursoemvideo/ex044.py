print('{:=^35}'.format(' LOJAS GUANABARA '))
valor = float(input('Qual é o valor da compra;? R$ '))
print('-'*35)
print('''\33[31m[1]\33[mDinheiro
\33[31m[2]\33[mDébito
\33[31m[3]\33[mCrédito''')
op = int(input('Qual será a forma de pagamento? '))
print('-'*35)
if op == 1:
    des = valor * 10 / 100
    print('Forma de pagamento: \33[34mDinheiro\33[m')
    print('O produto terá \33[32mR$ {:.2f}\33[m de desconto'.format(des))
    print('O valor total serã: \33[32mR$ {:.2f}'.format(valor - des))
elif op == 2:
    des = valor * 5 / 100
    print('Forma de pagamento: \33[34mDébito\33[m')
    print('O valor terá um desconto de \33[32mR$ {:.2f}\33[m'.format(des))
    print('O valor total será \33[32mR$ {:.2f}\33[m'.format(valor - des))
elif op == 3:
    op2 = str(input('Deseja parcelar? \33[31m[s/n]\33[m ')).strip()
    if op2.lower() == 'n':
        jur = 0.00
        print('Forma de pagamento \33[34mCrédito\33[m')
        print('O valor terá \33[33mR$ {:.2f}\33[m de juros'.format(jur))
        print('O valor total será de \33[32mR$ {:.2f}\33[m'.format(valor + jur))
    elif op2.lower() == 's':
        par = int(input('Deseja parcelar em quantas parcelas? '))
        if par == 0 or par > 24:
            print('\33[31mOpção invalida\33[m')
        elif par <= 3:
            jur = 0.00
            print('-'*35)
            print('Forma de pagamento \33[34mCrédito\33[m')
            print('O valor terá \33[33mR$ {:.2f}\33[m de juros'.format(jur))
            print('Números de parcelas: \33[32m{}\33[m'.format(par))
            print('Valor da parcela \33[32mR$ {:.2f}\33[m'.format(valor/par))
            print('O valor total será \33[32mR$ {:.2f}\33[m'.format(valor + jur))
        elif par > 3:
            jur = valor * 20 / 100
            print('-'*35)
            print('Forma de pagamentp \33[34mCrédito\33[m')
            print('O valor terá \33[31mR$ {:.2f}\33[m de juros (20%)'.format(jur))
            print('Número de parcelas: \33[32m{}\33[m'.format(par))
            print('O valor da parcela será de \33[32mR$ {:.2f}\33[m'.format((valor+jur)/par))
            print('O valor tota será \33[32mR$ {:.2f}\33[m'.format(valor+jur))
    else:
        print('\33[31mOpção invalida!\33[m')
else:
    print('\33[31mOpção invalida!\33[m')
