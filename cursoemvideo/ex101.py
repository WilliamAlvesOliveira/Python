# Crie um prohrama que tenha uma função chamada voto que vai receber como parametro
# o ano de nascimento de uma pessoa retornando
# um valor literal  se ela tem  direito ao voto, se é opcional, ou se é
# obrigatório (acima de 65 é opcional)

def voto(idade):
    '''Função que lera o ano de nascimento de uma pessoa é dirá a situação do voto
    se não pode votar, se o voto é opcional ou se é obrigatório'''
    from datetime import datetime
    idade = datetime.now().year - idade
    if idade < 16:
        return (f'Você tem {idade} anos, ainda não pode votar')
    elif idade < 18 or idade > 65:
        return (f'Você tem {idade} anos, seu voto é opcional')
    else:
        return (f'Você tem {idade} anos, seu voto é obrigatório')


#programa principal
nascimento = int(input('Informe o ano de nascimento: '))
print(voto(nascimento))