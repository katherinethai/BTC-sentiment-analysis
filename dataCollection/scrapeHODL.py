import urllib2
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')

base_url = 'https://news.hodlhodl.com/news?page={}'

# go to the website and find the last page
last_page = 13

page_urls = [base_url.format(i) for i in range(1, last_page+1)]

posFlairs = []
negFlairs = []

def getFileName(pos,num):
  if pos:
    return 'new_data/pos/pos_' + str(num) + '.txt'
  else:
    return 'new_data/neg/neg_' + str(num) + '.txt'

for url in page_urls:
  page = urllib2.urlopen(url)
  html = BeautifulSoup(page, 'html.parser')

  for li in html.select('li'):
    class_name = li['class'][0]

    #find headlines with pos/neg flags
    if class_name != 'noFlair':
      #get headline text
      temp = li.text.strip().split('(news)')[0]

      icon_div = list(li.children)[0]
      flag = list(icon_div.children)[0]['alt']

      #find out if flags are neg or pos
      if flag == 'Flair bullish':
        posFlairs.append(temp)
      else:
        negFlairs.append(temp)

print len(posFlairs)
for x, pos in enumerate(posFlairs):
  # x + 1 + num data points you already have
  f = open(getFileName(True,x+652),'w')
  f.write(pos)
  f.close()
  print pos

print ' '

print len(negFlairs)
for x, neg in enumerate(negFlairs): 
  # x + 1 + num of data points you already have
  f = open(getFileName(False,x+470),'w')
  f.write(neg)
  f.close()
  print neg





