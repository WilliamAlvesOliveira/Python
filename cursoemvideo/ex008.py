m=float(input('Digite uma distancia em metros: '))
print('A medida de {} metros correponde a:'.format(m))
print('{}Km \n{}hm \n{}dam \n{:.0f}dm \n{}cm \n{}mm'.format(m/1000, m/100, m/10, m*10, m*100,m*1000))