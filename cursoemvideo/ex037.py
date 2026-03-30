N = int(input('Digite um número: '))
print('\33[31m[1]\33[mpara Binário')
print('\33[31m[2]\33[mpara Octal')
print('\33[31m[3]\33[mpara Hexadecimal')
op = int(input('Selecione a opção de conversão: '))
if op == 1:
    print('O número \33[4m{}\33[m convertido para binãrio é \33[32m{}\33[m'.format(N,bin(N)[2:]))
elif op == 2:
    print('O número \33[4m{}\33[m convertido para Octal é \33[32m{}\33[m'.format(N,oct(N)[2:]))
elif op == 3:
    print('O número \33[4m{}\33[m convertido para hexadecimal é \33[32m{}\33[m'.format(N,hex(N)[2:]))
else:
    print('\33[31mInvalid Option\33[m')
print('Fim')
