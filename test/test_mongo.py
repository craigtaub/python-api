# pylint: disable=C0111

import unittest
from mock import MagicMock, patch, PropertyMock

class StubObject(object): pass


dataDict = {'name': 'NAME DATA'}
dataList = [dataDict]
findMock = MagicMock()
findMock.return_value = dataList
clubs = StubObject()
clubs.find = findMock
sportsbase = StubObject()
sportsbase.clubs = clubs
myObject = StubObject()
myObject.sportsbase = sportsbase
class TestMongo(unittest.TestCase):

    @patch('service.make_request')
    def test_fetchOne(self, mock):
        from mongo import fetchOne
        """Should call service with correct argument and return response"""
        mock.return_value = "RESPONSE DATA"

        self.assertEqual(fetchOne(), "RESPONSE DATA")
        mock.assert_called_with('one')

    @patch('pymongo.MongoClient', return_value=myObject)
    def test_fetch(self, mock_dont_call):
        """Should call mongo with expected id and return response"""
        from mongo import fetch

        self.assertEqual(fetch(), "NAME DATA")
        findMock.assert_called_with({'id': 9160})
        self.assertEqual(findMock.call_count, 1)


    @patch('mongo.dict_param')
    def test_testmethod(self, mock):
        from mongo import testMethod
        """Should return dictionary data"""
        mock.__getitem__.side_effect = lambda name: 'stub'
        result = testMethod()
        self.assertEqual(result, 'stub')


if __name__ == '__main__':
    unittest.main() # set so can run in isolation
