from sklearn.feature_extraction.text import TfidfVectorizer    # for TF-IDF implementation
import re    # for text cleaning]
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords    # to remove stopwords
import pandas as pd
import requests
import string
from bs4 import BeautifulSoup
import numpy as np

df = pd.read_csv("listofchains.csv")
names = df['Name'].values.tolist()
urls = df['URL']

def wikibot(url):
        url_open = requests.get(url)
        soup = BeautifulSoup(url_open.content, 'html.parser')
        details = soup('table', {'class':'infobox'})
        num_of_paras = len(soup('p'))
        document_string = ""
        for i in range(num_of_paras):
                document_string = document_string + soup('p')[i].text
        return document_string


documents = []
for i in range(len(urls)):
        documents.append(wikibot(urls[i]))
len(documents)
def text_preprocessing(text):
    text = text.lower()    # lowering the text
    text = re.sub(r"[^\w\s]", "", text)    # removing the puntuactions
    text = re.sub(r"[0-9]", "", text)    # removing the numbers
    s_word = stopwords.words('english')    
    text = [tex for tex in text.split() if tex not in s_word]    # removing the stopwords
    text = " ".join(text)
    while re.search(r'\b(.+)(\s+\1\b)+', text):    # removing the word repeating e.g. machine machine -> machine
        text = re.sub(r'\b(.+)(\s+\1\b)+', r'\1', text)
    return text

tf_idf_vector = TfidfVectorizer(ngram_range=(1, 3), stop_words='english')    # create instance of TfidfVectorizer
for i in range(len(documents)):
  documents[i] = text_preprocessing(documents[i])
tf_idf_transform = tf_idf_vector.fit_transform(documents)    # fitting the data(corpus) 
features_names = tf_idf_vector.get_feature_names_out()    # returning the features from the collection of docments
dense_list = tf_idf_transform.todense().tolist()     # value of TF-IDF
pd.set_option('display.max_columns', None)    # to show all the columns 
list_of_coins = names
df = pd.DataFrame(dense_list, columns=features_names, index=list_of_coins)

threshhold = 0.10

key_words = {}
# response = tf_idf_vector.transform([test_document])

# for col in response.nonzero()[1]:
#   print(features_names[col],' - ', response[0,col] )

feature_array = np.array(tf_idf_vector.get_feature_names_out())
# tfidf_sorting = np.argsort(response.toarray()).flatten()[::-1]

number_of_keywords = 3

# top_n = feature_array[tfidf_sorting][:number_of_keywords]

# print(top_n)


for i in range(len(documents)):
  response = tf_idf_vector.transform([documents[i]])
  tfidf_sorting = np.argsort(response.toarray()).flatten()[::-1]
  key_words[list_of_coins[i]]=feature_array[tfidf_sorting][:number_of_keywords]

print(key_words)
  
  





