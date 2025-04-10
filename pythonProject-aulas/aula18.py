teste = list()
teste.append('Gustavo')
teste.append('40')
galera = list()
galera.append(teste[:])
teste[0] = 'maria'
teste[1] = '22'
galera.append(teste[:])
teste[1] = '23'
print(galera)
print(teste)
