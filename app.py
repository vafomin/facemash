import random

from flask import Flask, render_template, url_for, redirect
from pymongo import MongoClient

app = Flask(__name__)

base = 'mongodb://admin:nimda@ds233895.mlab.com:33895/facemash'

client = MongoClient(base)
db = client["facemash"]


@app.route('/')
def index():
    f = db.data.find_one({"id": random.randint(1, db.data.count())})
    s = db.data.find_one({"id": random.randint(1, db.data.count())})
    if f == s:
        s = db.data.find_one({"id": random.randint(1, db.data.count())})
    return render_template('index.html', first=str(f["id"]), second=str(s["id"]))


@app.route('/vote/<v>')
def vote(v):
    vote = db.data.find_one({"id": int(v)})["vote"] + 1
    db.data.update({"id": int(v)}, {"$set":{"vote":vote}})
    print(db.data.find_one({"id": int(v)}))
    return redirect(url_for('index'), 302)


if __name__ == '__main__':
    app.run()
