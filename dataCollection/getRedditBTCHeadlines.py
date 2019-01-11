import requests
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf8')

r1 = requests.get('https://api.pushshift.io/reddit/search/submission/?subreddit=BTCNews&after=500d&size=500')

submissions = r1.json()['data']

titles = []

for x in range(0,500):
  titles.append(submissions[x]['title'])

with open('redditHeadlines.csv','wb') as file:
  for title in titles:
      file.write(title)
      file.write('\n')
