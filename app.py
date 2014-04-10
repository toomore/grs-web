# -*- coding:utf8 -*-
from flask import Flask
from grs import Stock


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
        stock = Stock(no)
        return u'%s %s' % stock.info

    return u'No stock'

if __name__ == '__main__':
    app.run(debug=1)

