#crie um programa que leia dois valores e mostre um menu
#1 somar 2 multiplicar 3 maior 4 novos números 5 sair do programa
#seu progama deve operar a opção solicitada em cada caso
op = 0
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
while op != 5:
    print('\33[31m[1]\33[mSomar valores {} e {}'.format(n1,n2))
    print('\33[31m[2]\33[mMultiplicar valores {} e {}'.format(n1,n2))
    print('\33[31m[3]\33[mMostrar qual dos valores é maior e menor {} e {}'.format(n1,n2))
    print('\33[31m[4]\33[mEscoher novos números')
    print('\33[31m[5]\33[mSair')
    op = int(input('Selecione uma opção: '))
    if op == 1:
        r = n1 + n2
        print('A soma entre os valores {} + {} é {}.'.format(n1,n2,r))
    elif op == 2:
        r = n1 * n2
        print('A multiplicação entre os valores {} x {} é {}'.format(n1,n2, r))
    elif op == 3:
        if n1 < n2:
            print('O menor valor é {}'.format(n1))
            print('E o maior é {}'.format(n2))
        elif n1 > n2:
            print('O menor número é {}'.format(n2))
            print('O maior número é {}'.format(n1))
        else:
            print('Ambos os números são iguais')
    elif op == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif op == 5:
        print('\33[34mFim\33[m')
    else:
        print('\33[31mOpção invalida!\33[m')
