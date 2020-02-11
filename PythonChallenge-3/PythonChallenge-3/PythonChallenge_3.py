import re
arquivo = open('arquivo.txt')
texto = arquivo.read()
p = re.compile('[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]')
print(p.findall(texto))
arquivo.close()