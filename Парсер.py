import requests
from bs4 import BeautifulSoup
import re
urls = open('urls.txt')

urls = urls.read()
urls = [x for x in urls.split()]

f = open('file.txt', 'a', encoding='utf-8')

soups = {}
info = []
for url in urls:
	page = requests.get(url)
	soup = BeautifulSoup(page.text, "html.parser")
	#print(soup)
	soups[url] = soup
	result = soup.find_all('ul')
	for res in result:
		res = res.get_text()
		
		f.write(res)


#Далее просим Qwen отсортировать как надо
