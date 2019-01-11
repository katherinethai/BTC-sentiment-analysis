import io
import re
import pandas
import nltk
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords

stop_words = stopwords.words('english')
tokenizer = RegexpTokenizer(r'\w+')

def process_text(headlines):
  tokens = []
  for line in headlines: 
    toks = tokenizer.tokenize(line)
    toks = [t.lower() for t in toks if t.lower() not in stop_words]
    toks = [t for t in toks if t]
    tokens.append(toks)
  return tokens

