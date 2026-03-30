#reescreva a função leiaint que fizemos no desfio 104. incluindo agora a
# possibilidade de digitação de um número inválido. faça uma função leiafoat também
def validação_inteiro():
    '''
    Função para validar números inteiros
    :return: retorna um número somente quando receber um número inteiro
    '''
    while True:
        valor = str(input('Digite um número: '))
        try:
            inteiro = int(valor)
            return inteiro
        except:
            print('Erro! Digite um número inteiro válido')


def validação_float():
    '''
    Função para validar um valor flutuante
    :return: retorna um valor flutuante
    '''
    while True:
        valor = input('Digite um número flutuante: ').replace(',',',').strip()
        try:
            real = float(valor)
            return real
        except:
            print('Digite um número flutuante válido')


#programa principal
número_inteiro = validação_inteiro()
print(f'Você digitou o número {número_inteiro}')
número_flutuante = validação_float()
print(f'Você digitou o número flutuante {número_flutuante:.2f}')
