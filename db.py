# Data Base Creator  💾
from pymongo import MongoClient

base = 'mongodb://localhost:21017'

client = MongoClient(base)
db = client["shortly"]

db.data

for i in range(1,9):
    db.data.save( {'id':i, 'vote':0} )
