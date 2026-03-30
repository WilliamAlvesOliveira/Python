print('\033[0;36m-='*16)
print('   Analisador de triângulos')
print('-='*16)
l1 = float(input('\033[mDigite o primeiro seguimento: '))
l2 = float(input('Digite o segundo seguimento: '))
l3 = float(input('Digite o terceiro seguimento: '))
print('\033[36m-'*32)
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('\033[0;32mPode formar um triângulo')
else:
    print('\033[31mNão pode formar um triângulo')
