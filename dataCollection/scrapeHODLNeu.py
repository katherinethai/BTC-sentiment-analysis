import urllib2
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')

base_url = 'https://news.hodlhodl.com/news?page={}'

# go to the website and find the last page
last_page = 90

page_urls = [base_url.format(i) for i in range(1, last_page+1)]

#num data points you already have -- for file naming
x = 1567

page = urllib2.urlopen('https://news.hodlhodl.com/news')
html = BeautifulSoup(page, 'html.parser')

for url in page_urls:
  page = urllib2.urlopen(url)
  html = BeautifulSoup(page, 'html.parser')

  for li in html.select('li'):
    div = list(li.children)[1]
    class_name = li['class'][0]

    article_type = div.span.span.text.strip()

    if class_name == 'noFlair' and article_type == '(news)':
      #get headline text
      temp = li.text.strip().split('(news)')[0]
      f = open('new_data/neu/neu_' + str(x+1) + '.txt','w')
      f.write(temp)
      f.close()
      print temp
      x = x + 1
  print url    

