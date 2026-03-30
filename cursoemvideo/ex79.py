#faça um çrograma em que o usuario possa digitar varios valores numéricos e cadastre em uma lista
#Caso ele ja esteja cadastrado ele não sera adicionado,
#no fim mostre todos os números únicos em ordem crescente]
lista = list()
while True:
    n = int(input('Adicione um número a lista: '))
    if n not in lista:
        lista.append(n)
        print('\33[32mO número foi adicionado!\33[m')
    else:
        print('\33[31mNúmero ja existente\33[m')
    op = str(input('Deseja  adicionar outro número?\33[31m[S/N]\33[m: ').strip().lower())[0]
    while op not in 'sn':
        print('\33[31mOpção invalida!\33[m')
        op = str(input('Deseja  adicionar outro número?\33[31m[S/N]\33[m: ').strip().lower())
    if op == 'n':
        break
lista.sort()
print('-'*30)
print(lista)
print('\33[04mFIM DO PROGRAMA!\33[m')
