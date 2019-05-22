# encoding: utf-8

import requests
from bs4 import BeautifulSoup
import nltk
from collections import Counter
import math
from flask import Flask, render_template, url_for
from contextlib import closing
from sqlite3 import dbapi2 as sqlite3

app = Flask(__name__)

DATABASE = 'crawling.db'

def connect_db():
    """Returns a new connection to the database."""
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    """Creates the database tables."""
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/crawl')
def crawlpage():
    result = crawl()
    return render_template('result.html',vectors=result,st1=sim,st2=sim2)
    
def crawl():
    url1 = 'https://github.com/m-ender/alice'
    url2 = 'https://aheui.readthedocs.io/en/latest/specs.en.html'
    url3 = 'https://github.com/stefan-hering/grid'
    url4 = 'https://github.com/catseye/Funge-98/blob/master/doc/funge98.markdown'

    urls = [url1, url2, url3, url4]
    soups = list()

    #print('soup start')

    for url in urls:
        page = requests.get(url)    #느림
        #print('soup1')
        soups.append(BeautifulSoup(page.content, 'html.parser'))
        #print('soup2')

    #print('soup middle')

    text1 = soups[0].find('article').getText()
    text2 = soups[1].find('div',attrs={'class':'section','id':'specification-of-aheui'}).get_text().replace('¶','')
    text3 = soups[2].find('article').getText()
    text4 = soups[3].find('article').getText()

    #print('soup end')

    texts = [text1, text2, text3, text4]

    #p1 = nltk.pos_tag(nltk.word_tokenize(text1))
    #c1 = [b for a,b in p1]
    #c1 = tuple(zip(*p1))[1]

    #lists = list()
    vectors = list()

    for text in texts:
        #print('nltk start')
        token=nltk.word_tokenize(text)
        #print('nltk middle')
        pt = nltk.pos_tag(token,tagset='universal') #느림
        #print('nltk end')
        cnt = Counter(b for a,b in pt)
        lst = list(cnt.items())
        lst.sort(key=lambda x:x[0])
        #lists.append(lst)
        vec = tuple(b for a,b in lst)
        #vec = tuple(zip(*lst))[1]
        vectors.append(vec)

    ##print(*zip(*lists),sep='\n')
    ##print(*zip(*vectors),sep='\n')

    return list(zip(enumerate(urls),vectors))

def sim(a, b):
    a,b = zip(*zip(a,b))
    inner_product = sum(x*y for x,y in zip(a,b))
    norm_mult = math.sqrt(sum(x*x for x in a)*sum(y*y for y in b))
    return inner_product/norm_mult

def sim2(a, b):
    a,b = zip(*zip(a,b))
    inner_product = sum(x*y for x,y in zip(a,b))
    norm = max(sum(x*x for x in a),sum(y*y for y in b))
    return inner_product/norm


if __name__ == '__main__':
    #init_db()
    app.run()