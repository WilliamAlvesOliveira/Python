##Croe um código em pythom que teste se o site pudim esta acessível pelo
# computador usado
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/watch?v=iqzI0Nc6Q2I')
except urllib.error.URLError:
    print('Deu Erro')
else:
    print('Tudo ok')
