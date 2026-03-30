#faça um ptograma que tenha a função notas que pode receber várias notas de um aluno
# e vai retornar um dicionário com as seguintes informações: 1-Quantidade de notas
# 2-A maior nota 3-A menos nota 4-A média da turma 5-A situação do aluno(opcopmaç)

def notas (*num, sit=False):
    '''
    --> Função para analisar as notas e situação de vários alunos.
    :param num: Recebe uma ou mais notas de aum aluno
    :param sit: Valor opcional para indicar se deve ou não adicionar a situação
    :return: Dicionário com as informações dos alunos
    '''

    aluno = dict()
    aluno['total'] = len(num)
    aluno['maior'] = max(num)
    aluno['menor'] = min(num)
    aluno['média'] = sum(num) / len(num)
    if sit == True:
        if aluno['média'] >= 7:
           aluno['situação'] = 'Boa'
        elif aluno['média'] >= 5:
           aluno['situação'] = 'Media'
        else:
           aluno['situação']='Ruim'
    return aluno


resp = notas(10,7.5,10,8,7.5)
print(resp)
help(notas)