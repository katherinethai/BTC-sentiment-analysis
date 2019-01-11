import io
import re
import pandas
import nltk
import json
from preprocessing import get_features1
from nltk.corpus import wordnet 
import sys
reload(sys)
sys.setdefaultencoding('utf8')

num_pos = 705
num_neg = 478
num_neu = 1723

pos_headlines = []
neg_headlines = []
neu_headlines = []

for x in range(1,num_pos+1):
  f = io.open('../data/txt/pos/pos_' + str(x) + '.txt', encoding='utf-8')
  text = f.read()
  f.close()
  pos_headlines.append(text)

for x in range(1,num_neg+1):
  f = io.open('../data/txt/neg/neg_' + str(x) + '.txt', encoding='utf-8')
  text = f.read()
  f.close()
  neg_headlines.append(text)

for x in range(1,num_neu+1):
  f = io.open('../data/txt/neu/neu_' + str(x) + '.txt', encoding='utf-8')
  text = f.read()
  f.close()
  neu_headlines.append(text)  

labeled_headlines = ([(headline,'pos') for headline in pos_headlines] + [(headline,'neg') for headline in neg_headlines] + [(headline,'neu') for headline in neu_headlines])
#shuffles the data
#random.shuffle(labeled_headlines)
length = len(labeled_headlines)

train_headlines, test_dev_headlines, test_headlines = labeled_headlines[:int(length*0.6)], labeled_headlines[int(length*0.6):int(length*0.8)], labeled_headlines[int(length*0.8):]

#saving your datasets -- make sure to comment out the shuffle when you're done!!!
with open('../data/json/train_headlines.json','w') as fp:
  json.dump(train_headlines, fp, indent=1)

with open('../data/json/test_dev_headlines.json','w') as fp:
  json.dump(test_dev_headlines, fp, indent=1)

with open('../data/json/test_headlines.json','w') as fp:
  json.dump(test_headlines, fp, indent=1)