import re
arquivo = open('arquivo.txt')
texto = arquivo.read()
p = re.compile('[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]')
print(p.findall(texto))
arquivo.close()