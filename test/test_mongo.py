# pylint: disable=C0111

import unittest
from unittest.mock import Mock
from mock import MagicMock, patch, PropertyMock
import asyncio

class StubObject(object): pass
dataList = {'name': 'NAME DATA'}
findMock = MagicMock()
def get_mock_coro(return_value): # required for async testing
    @asyncio.coroutine
    def mock_coro(*args, **kwargs):
        return return_value
    return Mock(side_effect=findMock, wraps=mock_coro) # assert on side effect of coroutine
clubs = StubObject()
clubs.find_one = get_mock_coro(dataList) # findMock
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

    @patch('motor.motor_asyncio.AsyncIOMotorClient', return_value=myObject)
    def test_fetch(self, mock_dont_call):
        """Should call mongo with expected id and return response"""
        from mongo import fetch

        result = asyncio.get_event_loop().run_until_complete(fetch('12'))

        self.assertEqual(result, "NAME DATA")
        findMock.assert_called_with({'id': 12})
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
