def dobro(valor=0):
    return valor * 2


def metade(valor=0):
    return valor / 2


def aumentar(valor=0):
    aumento = valor / 100 * 10
    return valor + aumento


def diminuir(valor=0):
    diminuição = valor / 100 * 13
    return valor - diminuição


def moeda(valor = 0, moeda = 'R$'):
    return (f'{moeda} {valor}').replace('.',',')