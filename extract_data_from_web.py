import pickle as pickle
import requests
import string
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
df = pd.read_csv("listofcoins.csv")
names = df['name'].values.tolist()
urls = df['url'].values.tolist()


def wikibot(url):
	url_open = requests.get(url)
	soup = BeautifulSoup(url_open.content, 'html.parser')
	num_of_paras = len(soup('p'))
	document_string = ""
	for i in range(num_of_paras):
		document_string = document_string + soup('p')[i].text
	return document_string

documents = []
for url in tqdm(urls):
	documents.append(wikibot(url))

with open('outfile', 'wb') as fp:
    pickle.dump(documents, fp)
