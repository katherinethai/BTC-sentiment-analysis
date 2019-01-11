import io
import re
import pandas
import nltk
import json
import random
from preprocessing import get_features1
import sys
reload(sys)
sys.setdefaultencoding('utf8') 

#change numbers here according to data -- at some point make this automatic pls
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
random.shuffle(labeled_headlines)
length = len(labeled_headlines)

train1, test1 = labeled_headlines[:int(length*.67)], labeled_headlines[int(length*.67):]
train2, test2 = labeled_headlines[:int(length*.33)] + labeled_headlines[int(length*.66):], labeled_headlines[int(length*.33):int(length*.66)]
train3, test3 = labeled_headlines[int(length*.33):], labeled_headlines[:int(length*.33)]

array = [[train1,'train1'],[train2,'train2'],[train3,'train3'],[test1,'test1'],[test2,'test2'],[test3,'test3']]


for i in range(0,6):
  with open('../data/json/' + array[i][1] + '.json','w') as fp:
    json.dump(array[i][0], fp, indent=1)





