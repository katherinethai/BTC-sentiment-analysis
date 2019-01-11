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

with open('../data/json/train1.json') as f:
  train_headlines1 = json.load(f)

with open('../data/json/test1.json') as f:
  test_headlines1 = json.load(f)

with open('../data/json/train2.json') as f:
  train_headlines2 = json.load(f)

with open('../data/json/test2.json') as f:
  test_headlines2 = json.load(f)

with open('../data/json/train3.json') as f:
  train_headlines3 = json.load(f)

with open('../data/json/test3.json') as f:
  test_headlines3 = json.load(f)


train_set1 = [(get_features1(h), kind) for (h, kind) in train_headlines1]
test_set1 =  [(get_features1(h), kind) for (h, kind) in test_headlines1]

train_set2 = [(get_features1(h), kind) for (h, kind) in train_headlines2]
test_set2 =  [(get_features1(h), kind) for (h, kind) in test_headlines2]

train_set3 = [(get_features1(h), kind) for (h, kind) in train_headlines3]
test_set3 =  [(get_features1(h), kind) for (h, kind) in test_headlines3]

classifier1 = nltk.NaiveBayesClassifier.train(train_set1)
acc1 = (nltk.classify.accuracy(classifier1, test_set1))*100
print("Classifier accuracy percent:" + str(acc1))

classifier2 = nltk.NaiveBayesClassifier.train(train_set2)
acc2 = (nltk.classify.accuracy(classifier2, test_set2))*100
print("Classifier accuracy percent:" + str(acc2))

classifier3 = nltk.NaiveBayesClassifier.train(train_set3)
acc3 = (nltk.classify.accuracy(classifier3, test_set3))*100
print("Classifier accuracy percent:" + str(acc3))

print ((acc1 + acc2 + acc3)/3)

# # Error Analysis
errors = []
for (headline,tag) in test_headlines1:
  guess = classifier1.classify(get_features1(headline))
  if guess != tag:
    errors.append( (tag, guess, headline) )

for (tag, guess, headline) in sorted(errors):
    print('correct={:<8} guess={:<8s} headline={:<30}'.format(tag, guess, headline))

# print ("--------")

# for (headline,tag) in test_headlines2:
#   guess = classifier2.classify(get_features1(headline))
#   if guess != tag:
#     errors.append( (tag, guess, headline) )

# for (tag, guess, headline) in sorted(errors):
#     print('correct={:<8} guess={:<8s} headline={:<30}'.format(tag, guess, headline))

# print ("--------")

# for (headline,tag) in test_headlines3:
#   guess = classifier3.classify(get_features1(headline))
#   if guess != tag:
#     errors.append( (tag, guess, headline) )

# for (tag, guess, headline) in sorted(errors):
#     print('correct={:<8} guess={:<8s} headline={:<30}'.format(tag, guess, headline))

def tag_list(dataset):
  return [tag for (headline, tag) in dataset]
def apply_tagger(dataset, classifier):
  return [classifier.classify(get_features1(headline)) for (headline,tag) in dataset]


gold = tag_list(test_headlines1)
test = apply_tagger(test_headlines1,classifier1)
cm = nltk.ConfusionMatrix(gold, test)
print(cm.pretty_format(sort_by_count=True, show_percents=True, truncate=9))
