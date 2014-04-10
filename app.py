# -*- coding:utf8 -*-
from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return u'Hello grs web!'

if __name__ == '__main__':
    app.run()

