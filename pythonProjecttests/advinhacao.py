from random import randint

computador = randint(0,1000)

print('Tente adivinhar o múmero')
jogador = int(input('Palpite [0 até 1000]: '))

while jogador != computador:
    print('Você ERROU! Meu número é maior.' if computador > jogador else
          'Você ERROU! Meu número é menor.')
    jogador = int(input('Tente novamente: '))
print('PARABÉNS, você acertou!')
