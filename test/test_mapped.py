# pylint: disable=C0111

import unittest
from mapped import process

class TestMapped(unittest.TestCase):
    def setUp(self):
        pass

    def test_first(self):
        """Test 12 returns 1200"""
        self.assertEqual(process(12), 1200)

    def test_second(self):
        """Test 13 returns 1300"""
        self.assertEqual(process(13), 1300)

if __name__ == '__main__':
    unittest.main() # set so can run in isolation
