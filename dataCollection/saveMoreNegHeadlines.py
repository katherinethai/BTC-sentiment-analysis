import csv

with open('negHeadlines.csv','rb') as csvfile:
  reader = csv.reader(csvfile, delimiter='\n')
  for x,row in enumerate(reader):
      f = open('../data/neg/neg_' + str(x+104) + '.txt','w')
      f.write(row[0])
      f.close()