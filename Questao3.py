import requests
from lxml import html

url = 'http://econpy.pythonanywhere.com/ex/001.html'

arquivo = open('links.txt', 'w')

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
webpage = html.fromstring(page.content)
hrefs = webpage.xpath('//a/@href')

arquivo.write(str(hrefs))

print(hrefs)
arquivo.close()