# pylint: disable=C0111

import unittest
from mock import MagicMock, patch, PropertyMock
# from mongo import fetch, fetchOne, testMethod
import mongo

class StubObject(object): pass

@patch('mongo.pymongo')
@patch('mongo.pymongo.MongoClient')
class TestMongo(unittest.TestCase):

    def setUp(self):
        print('setup')
        pass


    # @patch('service.make_request')
    # def test_fetchOne(self, mock_api_call):
    #     """Should call service with correct argument"""
    #     mock_api_call.return_value = "RESPONSE DATA"

    #     self.assertEqual(fetchOne(), "RESPONSE DATA")
    #     mock_api_call.assert_called_with('one')


    # @patch('pymongo.MongoClient')
    # def test_fetch(self, mock_api_call):
    #     """Should call mongo with expected id and return response"""
    #     dataDict = {'name': 'NAME DATA'}
    #     dataList = [dataDict]
    #     findMock = MagicMock()
    #     findMock.return_value = dataList
    #     clubs = StubObject()
    #     clubs.find = findMock
    #     sportsbase = StubObject()
    #     sportsbase.clubs = clubs
    #     myObject = StubObject()
    #     myObject.sportsbase = sportsbase
    #     mock_api_call.return_value = myObject

    #     self.assertEqual(fetch(), "NAME DATA")
    #     findMock.assert_called_with({'id': 9160})
    #     self.assertEqual(findMock.call_count, 1)

    # print('Setup')
    # @patch('mongo.pymongo')
    @patch('mongo.MongoClient')
    def test_fetch(self, mock_api_call):
        """X"""
        mock_api_call.__getitem__.side_effect = lambda name: 'STUB'
        mock_api_call.return_value = 'STUB'

        # mock.__getitem__.side_effect = lambda name: 'STUB'
        # mock.return_value = 'STUB'

        mongo.fetch()
        # self.assertEqual(fetch(), "NAME DATA")
        # findMock.assert_called_with({'id': 9160})
        # self.assertEqual(findMock.call_count, 1)


    # @patch('mongo.MongoClient')
    # @patch('mongo.dict_param')
    # def test_testmethod(self, api, apii):
    #     """Should X"""
    #     api.__getitem__.side_effect = lambda name: 'STUB'
    #     apii.return_value = 'STUB CLIENT'
    #     print('call function')
    #     testMethod()


if __name__ == '__main__':
    unittest.main() # set so can run in isolation
