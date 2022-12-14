import requests
import string
from bs4 import BeautifulSoup
import pandas as pd

df = pd.read_csv("listofcoins3.csv")
names = df['Name'].values.tolist()
urls = df['URL']


def wikibot(url):
	url_open = requests.get(url)
	soup = BeautifulSoup(url_open.content, 'html.parser')
	details = soup('table', {'class':'infobox'})
	num_of_paras = len(soup('p'))
	document_string = ""
	for i in range(num_of_paras):
		print(soup('p')[i].text)
		document_string = document_string + soup('p')[i].text
	return document_string

documents = []
#for i in range(len(urls)):
	#documents.append(wikibot(urls[i]))
wikibot("https://coinmarketcap.com/currencies/bitcoin/")

