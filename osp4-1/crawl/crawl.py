#!/usr/bin/python
#-*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Turing_Award'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find('table',class_='wikitable')
#print(type(table))
tr = table.find_all('tr')
#print(type(tr))
pairs=list()
year=None
for tag in tr[1:]:
    theYear = year
    year = tag.find('th')
    if not year:
        year = theYear
    
    found =tag.find_all('td')
    if found:
        rec,*_=found
        pairs.append((year.getText().strip(),rec.find('a').get_text('title'),re.sub('\[[0-9]*\]','',_[-1].get_text())))

for x in pairs:
    print(x[0],'{0:25}'.format(x[1]),'\t',repr(x[2]))