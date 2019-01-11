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

with open('../data/json/train_headlines.json') as f:
  train_headlines = json.load(f)

with open('../data/json/test_dev_headlines.json') as f:
  test_dev_headlines = json.load(f)

with open('../data/json/test_headlines.json') as f:
  test_headlines = json.load(f)

train_set = [(get_features1(h), kind) for (h, kind) in train_headlines]
test_dev_set =  [(get_features1(h), kind) for (h, kind) in test_dev_headlines]
test_set =  [(get_features1(h), kind) for (h, kind) in test_headlines]

classifier = nltk.NaiveBayesClassifier.train(train_set)

print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, test_dev_set))*100)

# most informative features
classifier.show_most_informative_features(15)

# Error Analysis
errors = []
for (headline,tag) in test_dev_headlines:
  guess = classifier.classify(get_features1(headline))
  if guess != tag:
    errors.append( (tag, guess, headline) )

for (tag, guess, headline) in sorted(errors):
    print('correct={:<8} guess={:<8s} headline={:<30}'.format(tag, guess, headline))


