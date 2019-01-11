import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
from nltk import punkt
import random
import sys
reload(sys)
sys.setdefaultencoding('utf8')

bull_headlines = []
bear_headlines = []
neutral_headlines = []

#preparing txt files
def fill_arrays(kind,num):
  for x in range(1,num+1):
    f = open('data/' + kind + '/' + kind + '_' + str(x) + '.txt','r')
    if kind == 'pos':
      bull_headlines.append(f.read())
    elif kind == 'neg':
      bear_headlines.append(f.read())
    else:
      neutral_headlines.append(f.read())

fill_arrays('pos',651)
fill_arrays('neg',469)
fill_arrays('neu',1221)

#headline should be all lowercase 
def headline_features(headline):
  tokens = nltk.word_tokenize(headline)
  words = [w.lower() for w in tokens]
  vocab = sorted(set(words))
  return dict([(word, True) for word in vocab])

labeled_headlines = ([(headline,'bull') for headline in bull_headlines] + [(headline,'bear') for headline in bear_headlines] + [(headline,'neutral') for headline in neutral_headlines])
random.shuffle(labeled_headlines)
length = len(labeled_headlines)

feature_sets = [(headline_features(h), kind) for (h, kind) in labeled_headlines]
train_set, test_dev_set, test_set = feature_sets[:int(length*0.6)], feature_sets[int(length*0.6):int(length*0.8)], feature_sets[int(length*0.8):]

classifier = nltk.NaiveBayesClassifier.train(train_set)

print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, test_dev_set))*100)

classifier.show_most_informative_features(15)
