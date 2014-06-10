# -*- coding:utf8 -*-
from flask import Flask
from grs import RealtimeTWSE
from grs import Stock
from urllib2 import URLError


app = Flask(__name__)

@app.route("/")
def index():
    return u'Hello grs web!'

@app.route("/stock", defaults={'no': None})
@app.route("/stock/", defaults={'no': None})
@app.route("/stock/<no>")
def stock_page(no):
    no = str(no)
    if no:
        try:
            stock = Stock(no)
            return u'%s %s' % stock.info
        except URLError:
            return u'No connection'

    return u'No stock'

@app.route("/rl/<no>")
def realtime(no):
    result = RealtimeTWSE(no)
    return u'<pre>%s</pre>' % result.data

if __name__ == '__main__':
    app.run(debug=1)

