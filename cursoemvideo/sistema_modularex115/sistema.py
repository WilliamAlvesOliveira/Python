from sistema_modularex115.biblioteca.interface import  *
from time import sleep

while True:
    resposta = menu(['Ver pessoas','Cadastrar nova pessoas','Sair do sistema'])
    if resposta == 1:
        print('Opção 1')
    elif resposta == 2:
        print('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do sistema... até logo!')
        break
    else:
        print('\33[31mERRO! digite uma opção válida.\33[m')
    sleep(1)
