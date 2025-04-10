#cie um pprograma que leia varios npumeros. O programa  devera mostrar quantos
#firan dugutadis e a soma deles ussando a flag . para saia 999
q = s = 0
while True:
    n = int(input('Digite um número \33[31m\33[m[\33[31m999\33[m para \33[4msair\33[m]: '))
    if n == 999:
        break
    q += 1
    s += n
print(f'A soma dos {q} números digitados foi de {s}')
