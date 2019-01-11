import io
import re
import pandas
import nltk
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
from nltk.corpus import wordnet 
import sys
reload(sys)
sys.setdefaultencoding('utf8')

stop_words = stopwords.words('english')
tokenizer = RegexpTokenizer(r'\w+')

synonyms = []
antonyms = []

for syn in wordnet.synsets("lose"): 
    for l in syn.lemmas(): 
        synonyms.append(l.name()) 
        if l.antonyms(): 
            antonyms.append(l.antonyms()[0].name()) 
  
print(set(synonyms)) 
print(set(antonyms)) 

def get_features1(headline):
  #tokenize into words
  toks = tokenizer.tokenize(headline)
  #lowercase
  toks = [t.lower() for t in toks if t.lower() not in stop_words]
  #remove numbers
  toks = [re.sub(r'\d+','',t) for t in toks]
  return dict([(word, True) for word in toks])

def get_features2(headline):
  #tokenize into words
  toks = tokenizer.tokenize(headline)
  #lowercase
  toks = [t.lower() for t in toks if t.lower() not in stop_words]
  #remove numbers
  toks = [re.sub(r'\d+','',t) for t in toks]
  return dict([(word, True) for word in toks])

