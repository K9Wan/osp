import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    url = 'https://github.com/joonion/osp01'
    res = requests.get(url)

    html = BeautifulSoup(res.content, 'html.parser')

    #태그 이름으로 검색하기
    html_title = html.find('title')
    #태그 속성으로 검색하기
    #html_body = html.find(attrs={'class':'application-main'})
    #tablebody=html_body.find(attrs={'class':'repository-content'}).find('tbody')
    #fnamelist=tablebody.find_all(attrs={'class':'js-navigation-item'})
    #fnamelist=list(map(lambda x:x.find(attrs={'class':'content'}).text,fnamelist))
    
    fnamelist=html.find_all(attrs={'class':'content'})
    fnamelist=list(map(lambda x:x.text,fnamelist))
    fnamelist=fnamelist[1:]
    title = html_title.text
    
    return render_template('home2.html', parsed_title=title, filenamelist=fnamelist)

