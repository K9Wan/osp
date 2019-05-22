##!/usr/bin/python
#-*- coding: utf-8 -*-

from konlpy.tag import Kkma
from konlpy.utils import pprint
from konlpy.tag import Twitter
from konlpy.tag import Okt

def myprint(lst):
    st = "["+lst[0]
    for i in lst[1:]:
        st = st + ", "+i
    st = st + "]"
    pprint (st.encode('utf-8'))

if __name__ == '__main__':
    mystring= u'최대한 가벼운 제품, 그러나 안전하고 튼튼한 제품을 골라야 한다. 오늘은 날씨가 좋다.'
    kkma = Kkma()
    myprint(kkma.sentences(mystring))
    mystr=u'아버지가방에들어가신다.'
    pprint(kkma.pos(mystr))
    mystr=u'아버지가 방에 들어가신다.'
    pprint(kkma.pos(mystr))
    twitter = Twitter()
    mystr=u'아버지가방에들어가신다.'
    pprint(twitter.pos(mystr))
    mystr=u'아버지가 방에 들어가신다.'
    pprint(twitter.pos(mystr))
    okt = Okt()
    mystr=u'아버지가방에들어가신다.'
    pprint(okt.pos(mystr))
    mystr=u'아버지가 방에 들어가신다.'
    pprint(okt.pos(mystr))
    



