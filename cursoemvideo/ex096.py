# Faça um programa que tenha uma função chamada área(), que receba as dimensões
# de um terreno retanfular( largura e comprimento) e mostre a área do terreno;

def área(largura,comprimento):
    a= largura * comprimento
    print(f'A área de um terreno com {largura} por {comprimento} é {a}')



print('Controle de terrenos')
print('-'*20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
área(l,c)