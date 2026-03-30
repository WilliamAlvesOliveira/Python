from ex115.modulos.interface import *

def arquivoexiste(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(f'Ocorreu um erro. O arquivo não foi criado!')
    else:
        print('Arquivo criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f'{cores("vermelho")}Erro ao ler o arquivo{cores()}')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(a.read())