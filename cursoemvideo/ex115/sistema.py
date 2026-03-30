#crie um pequeno sistema modularizado que permite cadastrar pessoas pelo seu
# nome e idade em um arquivo de texto simples. O sistema só vai ter duas opções:
# cadastrar ums nova pessoa e listar todas as pessoas cadastradas
from select import select

from modulos.arquivo import*

arq = 'curso_em_videotxt'
if not arquivoexiste(arq):
        criararquivo(arq)

menu = ['Ver pessoas cadastrada',
        'Cadastrar nova pessoa',
        'Sair do sistema']

cabeçalho('MENU PRINCIPAL')

opções(menu)
op = resposta()
if op == 1:
        lerArquivo(arq)
elif op == 2:
        print('Opção 2')
        print(linha())
elif op == 3:
        print('Saindo do programa...')
        print(linha())
        exit()
else:
        print(f'{cores("vermelho")}Opção Invalida!!!{cores()}')
        print(linha())
