def dinheiro(str):
    try:
        str = str.replace(',','.')
        dinheiro =  float(str)
        return dinheiro
    except ValueError:
        print('Erro! preço inválido')
        dinheiro = 0.00
        return dinheiro


def dobro(valor=0):
    valor *= 2
    return moeda(valor)


def metade(valor=0):
    valor /= 2
    return moeda(valor)


def aumentar(valor=0,taxa=0):
    aumento = valor + (valor * taxa / 100)
    return moeda(aumento)


def diminuir(valor=0,taxa=0):
    diminuição = valor  - (valor * taxa / 100)
    return moeda(diminuição)

def moeda(valor):
    return f'R$ {valor:.2f}'.replace('.',',')