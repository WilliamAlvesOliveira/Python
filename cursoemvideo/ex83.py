#Droe um programa onde o usuário digite uma expressão qualquer que use parenteses
#seu aplicativo deverá analisar se a expressão pssada está
# #com os parestêses abertos e fechados na ordem correta
expressão = str(input('Digite uma expressão: '))
pilha = []
for simb in expressão:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('\33[32mSua expressão está válida!\33[m')
else:
    print('\33[31mSua expressão está incorretaQ\33[m')
