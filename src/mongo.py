import service
import motor.motor_asyncio

dict_param = {
    'data': 'real'
}

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://192.168.99.100:32775')
db = client.sportsbase
clubs = db.clubs

def testMethod():
    return dict_param['data']
    
async def fetch(my_id):
    cursor = await clubs.find_one({"id": int(my_id)})
    return cursor['name']

def fetchOne():
    return service.make_request('one')

