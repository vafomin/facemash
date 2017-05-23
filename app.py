import random

from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

base = 'mongodb://admin:nimda@ds233895.mlab.com:33895/facemash'

client = MongoClient(base)
db = client["facemash"]


@app.route('/')
def hello_world():
    f = db.data.find_one({"id": random.randint(1, db.data.count())})
    s = db.data.find_one({"id": random.randint(1, db.data.count())})
    if f == s:
        s = db.data.find_one({"id": random.randint(1, db.data.count())})
    return render_template('index.html', first=str(f), second=str(s))


if __name__ == '__main__':
    app.run()
