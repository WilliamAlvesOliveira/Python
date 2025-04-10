#criwe um programa que leia nome, ano de nascimento, a carteira de trabalho e
# cadastre-os em um dicionário se por acaso a CTPS for diferente de zero,
# o dicionário  receberá também o ano de contratação e o salário.
# calcule e acrescente além da idade. com quantos anos a pessoa vai se aposentar. 35anos de contribuição
from datetime import datetime
pessoa = {}

#Cadastri
pessoa['nome'] = str(input('Insira o seu nome: '))
nascimento = int(input('Insira o ano de nascimento: '))
pessoa['idade'] = datetime.now().year - nascimento
pessoa['CTPS'] = int(input("Nº da Carteira de Trabalho: "))
if pessoa['CTPS'] != 0:
    pessoa['colaboração'] = int(input('Qual o ano do primeiro registro: '))
    pessoa['salário'] = float(input('Qual é o salário atual: '))
    pessoa['aposentadoria'] = pessoa['colaboração']+35
    if datetime.now().year - pessoa['colaboração'] >= 35:
        pessoa['situação'] = 'apto'
    else:
        pessoa['situação'] = 'inapto'

#saída
print('Analisando')
print('-'*30)
print(f'Nome: {pessoa['nome']}')
print(f'Idade: {pessoa['idade']}')
print(f'CTPS: {pessoa['CTPS']}')
if pessoa['CTPS'] > 0:
     print(f'Salário atual: {pessoa['salário']}')
     print(f'Situação: {pessoa['situação']}')
     print(f'Ano de aposentadoria: {pessoa['aposentadoria']}')
     print(f'Se aposenta-ra com: {pessoa['aposentadoria'] -  nascimento}')
else:
    print('Você náo possui tempo de colaboração')
print('FIM DO PROGRAMA')
