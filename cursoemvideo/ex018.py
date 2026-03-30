from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja '))
print('O angulo de {:.2f} tem o SENO de {:.2f}\n o COSENO de {:.2f}\n e a TANGENTE de {:.2f}'.format(ang,sin(radians(ang)),cos(radians(ang)), tan(radians(ang))))
