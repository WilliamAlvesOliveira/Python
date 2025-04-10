#faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro emostre uma mnsagem com
# tamanho adaptável;

def escreva(mensagem):
    tam = len(mensagem)+4
    print('-'*tam)
    print(f'  {mensagem}')
    print('-' *tam)


escreva('william')
escreva('let it rip')