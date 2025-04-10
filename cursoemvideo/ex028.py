from random import randint
from time import sleep
rn = randint(0,5)
n = int(input('Em que número eu estou pensando? [0 a 5]: '))
print("PROCESSANDO...")
sleep(2)
if n == rn:
    print('Eu pensei em {}\nPARABÉNS você VENCEU!!!'.format(rn))
else:
    print('Eu pensei em {}\nVocê Perdeu!!!'.format(rn))
