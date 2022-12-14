from sklearn.feature_extraction.text import TfidfVectorizer    # for TF-IDF implementation
import re    # for text cleaning]
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords    # to remove stopwords
import pickle as pickle
from tqdm import tqdm


with open('outfile', 'rb') as dp:
    documents = pickle.load(dp)

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
for i in tqdm(range(len(documents))):
  documents[i] = text_preprocessing(documents[i])

with open('processed_documents', 'wb') as fp:
    pickle.dump(documents, fp)