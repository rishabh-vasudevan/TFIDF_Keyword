# TFIDF_Keyword
Algorithm to extract data from links and running tfidf to find keywords
To run this first make sure you add all the names and urls in the csv to the chains you want to extract the key words for

You will have to make a csv with name and url, which contains the names of the coins and the url from where the data needs to be extracted

To run this 
```
pip install -r requirements.txt

python extract_data_from_web.py

python text_preprocessing.py

python tfidfoncoins.py
```
*note: make sure right csv is being called in the `tfidf.py` file*

The scrapper file is embedded inside `tfidf.py` file, this was just made for testing
