from sklearn.feature_extraction.text import TfidfVectorizer    # for TF-IDF implementation
import pandas as pd
import numpy as np
import pickle as pickle
from tqdm import tqdm
import csv

df = pd.read_csv("listofcoins.csv")
names = df['name'].values.tolist()

with open('processed_documents', 'rb') as dp:
    documents = pickle.load(dp)

tf_idf_vector = TfidfVectorizer(ngram_range=(1, 3), stop_words='english')    # create instance of TfidfVectorizer
tf_idf_transform = tf_idf_vector.fit_transform(documents)    # fitting the data(corpus) 
features_names = tf_idf_vector.get_feature_names_out()    # returning the features from the collection of docments


key_words = {}
# response = tf_idf_vector.transform([test_document])

# for col in response.nonzero()[1]:
#   print(features_names[col],' - ', response[0,col] )

feature_array = np.array(tf_idf_vector.get_feature_names_out())
# tfidf_sorting = np.argsort(response.toarray()).flatten()[::-1]

number_of_keywords = 100

# top_n = feature_array[tfidf_sorting][:number_of_keywords]

# print(top_n)


for i in tqdm(range(len(documents))):
  response = tf_idf_vector.transform([documents[i]])
  tfidf_sorting = np.argsort(response.toarray()).flatten()[::-1]
  # print(response.toarray())

  key_words[names[i]]=feature_array[tfidf_sorting][:number_of_keywords].tolist()
  # [key_words[names[i]][j] = (key_words[names[i]][j], response.toarray()[tfidf_sorting[j]]) for j in range(len(key_words[names[i]]))]
  tfidf_value = response.toarray().flatten().tolist()
  for j in range(len(key_words[names[i]])):
    key_words[names[i]][j] = (key_words[names[i]][j], tfidf_value[tfidf_sorting[j]])

  # [for i in range(key_words[])]


with open('keywords.csv', 'w') as f:  # You will need 'wb' mode in Python 2.x
    w = csv.writer(f)
    w.writerows(key_words.items())
  





