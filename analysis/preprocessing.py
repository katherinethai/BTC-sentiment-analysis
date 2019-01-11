import io
import re
import pandas
import nltk
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
from nltk.corpus import wordnet 
from nltk.stem.lancaster import LancasterStemmer
import sys
reload(sys)
sys.setdefaultencoding('utf8')

stop_words = stopwords.words('english')
stop_words.extend([''])
exceptions = set(('no', 'nor', 'not','below','above','against','after','up','down','over','under','again','more','few'))
stop = set(stop_words) - exceptions

tokenizer = RegexpTokenizer(r"\w+(?=n\'t)|n\'t|\w+(?=')|\'\w+|\w+")

loss_words = ['hack','regulate','ban']
gain_words = ['launch','rise','support']
neg_words = ['no','refuse','reject','not','nor','n\'t']

lancaster_stemmer = LancasterStemmer()

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
  #get stems
  toks = [lancaster_stemmer.stem(t) for t in toks]
  return dict([(word, True) for word in toks])

def get_features3(headline):
  #tokenize into words
  toks = tokenizer.tokenize(headline)
  #lowercase and different set of stop words
  toks = [t.lower() for t in toks if t.lower() not in stop]
  #remove numbers
  toks = [re.sub(r'\d+','',t) for t in toks]
  #get stems
  toks = [lancaster_stemmer.stem(t) for t in toks]
  return dict([(word, True) for word in toks])

def get_features4(headline):
  features = {}
  #tokenize into words
  toks = tokenizer.tokenize(headline)
  neg_count = 0
  #lowercase and different set of stop words
  toks = [t.lower() for t in toks if t.lower() not in stop]
  for t in toks:
    #remove numbers, get stems
    t = re.sub(r'\d+','',t)
    t = lancaster_stemmer.stem(t)
    #mark if there are loss words
    if t in loss_words: 
      loss = True 
      neg_count += 1
    else: 
      loss = False
    #mark if gain words 
    gain = True if t in gain_words else False
    #mark if neg words
    if t in neg_words: neg_count += 1
    neg = True if neg_count % 2 == 1 else False

    features[t] = True
    # features['loss_words'] = loss
    # features['gain_words'] = gain
    features['neg'] = neg

  return features

