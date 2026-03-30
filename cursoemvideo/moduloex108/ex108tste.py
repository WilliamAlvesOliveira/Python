#adapte o código do exercicio 107. criando uma função chamada moeda()
# que consiga mostrar os valores como um valor monetário formatado
from moeda import dobro, metade, aumentar, diminuir, moeda

preço = str(input('Digite um preço: R$ ')).replace(',','.')
print(f'O dobro de {moeda(moeda(preço))} é {moeda(dobro(preço))}')
print(f'A metade de {moeda(moeda(preço))} é {moeda(metade(preço))}')
print(f'Aumentando 10% de R$ {preço:.2f} teremos R$ {aumentar(preço):.2f}')
print(f'Diminuindo 13% de R$ {preço:.2f} teremos R$ {diminuir(preço):.2f}')