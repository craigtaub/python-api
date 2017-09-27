# pylint: disable=C0111

import unittest
from mapped import process

class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def test_first(self):
        self.assertEqual(process(12), 1200)

    def test_second(self):
        self.assertEqual(process(13), 1300)

if __name__ == '__main__':
    unittest.main() # set so can run in isolation
