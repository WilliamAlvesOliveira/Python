#crie um programa que tenha uma funçãio chamada leia int.que vai funcionar de
# forma semelhante a função input do python
# só que fazendo a validação para aceitar apenas valores numericos

def leiaint(v):
    '''
    função para validação de números inteiros
    :param v: número de entrada do usuário
    :return: número inteiro validado
    '''

    while True:
        if v.isnumeric():
             v = int(v)
             break
        else:
            v = input('\33[31mERRO!\33[m, digite apenas números inteiros: ')
    return  v


n = leiaint(input('Digite um número: '))
print(f'O número digitado foi \33[34m{n}\33[m')
