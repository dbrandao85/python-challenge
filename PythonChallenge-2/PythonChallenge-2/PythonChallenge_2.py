from collections import Counter
arquivo = open('caracter.txt')
texto = arquivo.read()
c = Counter(texto)
resultado = (c.most_common())
print(resultado)
arquivo.close()