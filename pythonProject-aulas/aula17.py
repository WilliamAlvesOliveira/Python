num = [2,5,9,1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.insert(2,2)
num.remove(2)#ele vai varrer a lista e eliminar a primeira ocoremcia do número 2. nãp p número que está na key 2
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')