from flask import Flask
from flask import render_template
from flask import redirect, url_for
from flask import request

app = Flask(__name__)

@app.route('/')
def init():
    return redirect(url_for('home11'))

@app.route('/home')
def home11():
    return render_template('home.html', name=None)

@app.route('/info', methods=['POST', 'GET'])
def info():
    error = None
    if request.method == 'POST':
        myname = request.form['name']
        mynum = request.form['num']
        return render_template('info.html', name=myname, num11=mynum)
    else:
        myname = request.args.get('name')
        return render_template('info.html', name=myname)

