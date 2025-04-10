materiais = ('Lápis', 1.75,'Borracha',2.00, 'Caderno', 15.00,'Estojo', 25.00,
             'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.00, 'Canetas',
             22.39, 'Livro', 34.90)

print('-'*34)
print(' '*7,'Lista de preços')
print('-'*34)

for c in range(0,len(materiais)):
    if c % 2 == 1:
        print(f'.'*(20-len(materiais)),'R$', materiais[c])
    else:
        print(materiais[c],end='')
print('-'*34)

