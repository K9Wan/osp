import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    url = 'https://ko.wikipedia.org/wiki/웹 크롤러'
    res = requests.get(url)

    html = BeautifulSoup(res.content, 'html.parser')
    return render_template('home.html', parsed_page=html)

