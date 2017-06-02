# Data Base Creator  💾
import os
from pymongo import MongoClient

path, dirs, files = os.walk("app/static/images").next()
count = len(files)

base = 'mongodb://localhost:21017'

client = MongoClient(base)
db = client["shortly"]

db.data

for i in range(1,count):
    db.data.save( {'id':i, 'vote':0} )
