preço = float(input('Qual é o prço do produto? R$ '))
desconto = preço*5/100
print('O preço desse produto custa R$  {:.2f}\nna promoção com  5% de desconto vai custar R$ {:.2f}'.format(preço,preço - desconto))
