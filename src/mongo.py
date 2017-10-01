import service
import pymongo

dict_param = {
    'data': 'real'
}

client = pymongo.MongoClient("mongodb://192.168.99.100:32770")
db = client.sportsbase
clubs = db.clubs

def testMethod():
    return dict_param['data']
    
def fetch():
    cursor = clubs.find({"id": 9160})
    return cursor[0]['name']

def fetchOne():
    return service.make_request('one')

