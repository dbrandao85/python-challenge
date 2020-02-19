import urllib.request
html = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/channel.html').read()
print(html)