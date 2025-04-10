nome = str(input('Digite o seu nome completo'))
print('Muito prazer',nome)
print('Seu primeiro nome é: ',nome.split()[0])
print('Seu ultimo nome é: ',nome.split()[len(nome.split())-1])