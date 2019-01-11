import io
import re
import pandas
import nltk
import json
from preprocessing import get_features4
from preprocessing import get_features4
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


train_set1 = [(get_features4(h), kind) for (h, kind) in train_headlines1]
test_set1 =  [(get_features4(h), kind) for (h, kind) in test_headlines1]

train_set2 = [(get_features4(h), kind) for (h, kind) in train_headlines2]
test_set2 =  [(get_features4(h), kind) for (h, kind) in test_headlines2]

train_set3 = [(get_features4(h), kind) for (h, kind) in train_headlines3]
test_set3 =  [(get_features4(h), kind) for (h, kind) in test_headlines3]

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
def tag_list(dataset):
  return [tag for (headline, tag) in dataset]
def apply_tagger(dataset, classifier):
  return [classifier.classify(get_features4(headline)) for (headline,tag) in dataset]

# errors1 = []
# for (headline,tag) in test_headlines1:
#   guess = classifier1.classify(get_features4(headline))
#   if guess != tag:
#     errors1.append( (tag, guess, headline) )

# for (tag, guess, headline) in sorted(errors1):
#     print('correct={:<8} guess={:<8s} headline={:<30}'.format(tag, guess, headline))

# print ("--------")

# errors2 = []
# for (headline,tag) in test_headlines2:
#   guess = classifier2.classify(get_features4(headline))
#   if guess != tag:
#     errors2.append( (tag, guess, headline) )

# for (tag, guess, headline) in sorted(errors2):
#     print('correct={:<8} guess={:<8s} headline={:<30}'.format(tag, guess, headline))

# print ("--------")

# errors3 = []
# for (headline,tag) in test_headlines3:
#   guess = classifier3.classify(get_features4(headline))
#   if guess != tag:
#     errors3.append( (tag, guess, headline) )

# for (tag, guess, headline) in sorted(errors3):
#     print('correct={:<8} guess={:<8s} headline={:<30}'.format(tag, guess, headline))

gold1 = tag_list(test_headlines1)
test1 = apply_tagger(test_headlines1,classifier1)
cm1 = nltk.ConfusionMatrix(gold1, test1)
print(cm1.pretty_format(sort_by_count=True, show_percents=True, truncate=9))

gold2 = tag_list(test_headlines2)
test2 = apply_tagger(test_headlines2,classifier2)
cm2 = nltk.ConfusionMatrix(gold2, test2)
print(cm2.pretty_format(sort_by_count=True, show_percents=True, truncate=9))

gold3 = tag_list(test_headlines3)
test3 = apply_tagger(test_headlines3,classifier3)
cm3 = nltk.ConfusionMatrix(gold3, test3)
print(cm3.pretty_format(sort_by_count=True, show_percents=True, truncate=9))
