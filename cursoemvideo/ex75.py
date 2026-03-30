par = primeiro = segundo = 0
tup=  (int(input('Digite um número: ')),int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
n1 = tup[0]
if tup[1] != n1:
    n2 = tup[1]
else:
    if tup[2] != n1:
        n2 = tup[2]
    else:
        if tup[3] != n1:
            n2 = tup[3]
        else:
            n2 = 0
for c in range(0,4):
    if  tup[c] % 2 == 0 :
        par += 1
    if tup[c] == n1:
        primeiro += 1
    if tup[c] == n2:
        segundo += 1

print(f'Você digitou os valores {tup}')
print(f'O valor {n1} apareceu {primeiro} vazes')
if primeiro != 4:
    print(f'O valor {n2} apareceu {segundo} vazes')
print(f'Valores pares digitados foram {par}')
