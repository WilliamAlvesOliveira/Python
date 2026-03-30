#crie um modulo chamado moeda.py. que tenha as funções incorporadas aumentar
# diminuir dobro metade
#faça um programa que importe esse modulo e use uma dessas funçoes
import moedas
from moedas import moeda
preço = moedas.dinheiro(str(input('Digite um preço: R$')))
print(f'O dobro de {moeda(preço)} é {moedas.dobro(preço)}')
print(f'A metade de {moeda(preço)} é R$ {moedas.metade(preço)}')
print(f'Aumentando 10% de {moeda(preço)} teremos {moedas.aumentar(preço,10)}')
print(f'Diminuindo 13% de {moeda(preço)} teremos {moedas.diminuir(preço,13)}')
