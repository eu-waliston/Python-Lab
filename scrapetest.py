from urllib.request import urlopen

html = urlopen('https://www.google.com.br')
print(html.read())