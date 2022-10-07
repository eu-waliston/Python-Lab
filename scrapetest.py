from urllib.request import urlopen

html = urlopen('https://www.ufsm.br')
print(html.read())