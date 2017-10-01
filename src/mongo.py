import service
# import pymongo
from pymongo import MongoClient

dict_param = {
    'data': 'real'
}

print('called')
# print('pymongo', pymongo)
client = MongoClient("mongodb://192.168.99.100:32770")
print('CLIENT TOP', client)
db = client.sportsbase
clubs = db.clubs

def testMethod():
    print('real MongoClient:', pymongo.MongoClient)
    print('test_param', dict_param['data'])
    
def fetch():
    # client = MongoClient()
    # print('CLIENT INNER', client)
    # BAD, connect each time called
    # db = client.sportsbase
    # clubs = db.clubs
    # print('HERE', clubs)
    cursor = clubs.find({"id": 9160})
    return cursor[0]['name']
    # return 1

def fetchOne():
    return service.make_request('one')

