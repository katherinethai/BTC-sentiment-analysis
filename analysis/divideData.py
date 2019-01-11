import io
import re
import pandas
import nltk
import json
import random
from preprocessing import process_text 

#change numbers here according to data -- at some point make this automatic pls
num_pos = 705
num_neg = 478
num_neu = 1723

pos_headlines = []
neg_headlines = []
neu_headlines = []

for x in range(1,num_pos+1):
  f = io.open('new_data/pos/pos_' + str(x) + '.txt', encoding='utf-8')
  text = re.sub(r'\d+','',f.read())
  f.close()
  pos_headlines.append(text)

for x in range(1,num_neg+1):
  f = io.open('new_data/neg/neg_' + str(x) + '.txt', encoding='utf-8')
  text = re.sub(r'\d+','',f.read())
  f.close()
  neg_headlines.append(text)

for x in range(1,num_neu+1):
  f = io.open('new_data/neu/neu_' + str(x) + '.txt', encoding='utf-8')
  text = re.sub(r'\d+','',f.read())
  f.close()
  neu_headlines.append(text)  

pos_toks = process_text(pos_headlines)
neg_toks = process_text(neg_headlines)
neu_toks = process_text(neu_headlines)

labeled_headlines = ([(headline,'pos') for headline in pos_toks] + [(headline,'neg') for headline in neg_toks] + [(headline,'neu') for headline in neu_toks])

#shuffles the data
random.shuffle(labeled_headlines)

length = len(labeled_headlines)

def headline_features(words):
  vocab = sorted(set(words))
  return dict([(word, True) for word in vocab])

feature_sets = [(headline_features(h), kind) for (h, kind) in labeled_headlines]
train_set, test_dev_set, test_set = feature_sets[:int(length*0.6)], feature_sets[int(length*0.6):int(length*0.8)], feature_sets[int(length*0.8):]

#saving your datasets -- make sure to comment out the shuffle when you're done!!!
with open('train_set.json','w') as fp:
  json.dump(train_set, fp, indent=1)

with open('test_dev_set.json','w') as fp:
  json.dump(test_dev_set, fp, indent=1)

with open('test_set.json','w') as fp:
  json.dump(test_set, fp, indent=1)
