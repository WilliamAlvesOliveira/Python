print('\33[32mALUGUEL DE CARROS\33[m')
print('-'*30)
d = int(input('Quantos dia você alugou carro?: '))
km =  float(input('Quanto Km você rodou com ele?: '))
v = d * 60 + km * 0.15
print('O valor total a pagar é \33[32mR${:.2f}\33[m'.format(v))
