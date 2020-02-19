import urllib.request
import re
#valor= '12345'
#valor= '8022'
valor ='63579'
i = 1
while i < 400:
    with urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+valor) as response:
        print(i)
        html = response.read()
        print(html.decode("utf-8"))
        numeros = re.compile('[0-9]+')
        temporario = numeros.findall(html.decode("utf-8"))
        valor = temporario[0]
        print(valor)
        i += 1