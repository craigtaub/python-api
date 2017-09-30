from pymongo import MongoClient
from service import make_request

client = MongoClient("mongodb://192.168.99.100:32770")
db = client.sportsbase
clubs = db.clubs

def fetch():
    # make_request()
    cursor = clubs.find({"id": 9160})
    return cursor[0]['name']

