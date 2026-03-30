def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\33[31mErro! Digite um número inteiro válido\33[m')
            continue
        except KeyboardInterrupt:
            print()
            print('O usúario não quis indicar um valor')
            exit()
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg).replace(',','.').strip())
        except (ValueError, TypeError):
            print('\33[31mErro! Digite um número flutuante válido.\33[m')
            continue
        except KeyboardInterrupt:
            print()
            print('O usúario não quis indicar um valor')
            exit()
        else:
            return n


num = leiaint('Digite um valor: ')
print(f'O valor digitado foi {num}')
num = leiafloat('Digite um valor flutuante: ')
print(f'O valor flutuante digitado foi {num}')