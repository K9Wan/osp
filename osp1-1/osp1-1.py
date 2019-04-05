from flask import Flask
from flask import render_template
from flask import redirect, url_for

app = Flask(__name__)

@app.route('/')
def init():
    return redirect(url_for('home11'))

@app.route('/home')
def home11():
    return render_template('home.html', name=None)

@app.route('/about/<info>')
def about1(info):
    return render_template('about.html', i=info)
