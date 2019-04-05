from flask import Flask
from flask import render_template
from flask import redirect, url_for
from flask import request

app = Flask(__name__)

@app.route('/')
def init_wordfind():
    return redirect(url_for('wordfind'))

@app.route('/wordfindinghome')
def wordfind():
    return render_template('wfhome.html')

@app.route('/result', methods=('POST',)) 
#Allowed methods have to be iterables of strings, for example:@app.route(..., methods=["POST"])
def result():
    if request.method == 'POST':
        word = request.form['finding']
        para = request.form['paragraph']
        existing = word.replace(' ', '') in para.replace(' ', '')
        return render_template('showresult.html', wordfinding=word, word_exists=existing)

