import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    url = 'https://ko.wikipedia.org/wiki/웹 크롤러'
    res = requests.get(url)

    html = BeautifulSoup(res.content, 'html.parser')

    #태그 이름으로 검색하기
    html_title = html.find('title')
    #태그 속성으로 검색하기
    html_body = html.find(attrs={'class':'mw-parser-output'})

    title = html_title.text
    body = html_body.find('p').text
    body2 = html_body.find('p')
    return render_template('home1.html', parsed_title=title, parsed_body=body, body2=body2)

