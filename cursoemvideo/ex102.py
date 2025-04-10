# Crie um programa que tenha uma função chamada fatorial que receba dois
# parametros: o primeiro que indique o número a calcular e o pitrp chamdo show que
# sera um valor lógivo(opcional) indicando se será mostrado ou não na tela o ptocesso
# de cálculo do fatorial

def fatorial (n, show=False):
    """ ->calcula o fatorial de um número
    param n: o npumero que deve ser calculado
    param show (opcional) para mostrar ou não a conta
    return: o valor fatorial do número
    """

    f =1
    print(f'{n}! = ',end='')
    for c in range(n, 0, -1):
        f *= c

        if show:
            print(f'{c}',end=' ')
            if c > 1:
                print('x ', end='')
            else:
                print(' = ',end=' ')
    return f

#programa principal
numero = int(input("Digite um número para ver o seu valor fatorial: "))
print(fatorial(numero))