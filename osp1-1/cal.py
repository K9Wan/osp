from flask import Flask
app1 = Flask(__name__)

@app1.route('/')
def init():
    today = "Friday"
    return 'Today is %s' % today

@app1.route('/<num>')
def cal(num):
    n=int(num)
    return '{0} + {0} = {1}'.format(n, 2*n)

