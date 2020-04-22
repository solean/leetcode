from implement_strStr_28 import strStr
import unittest

class TestImplementStrStr(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(strStr('test', ''), 0)

    def test_not_found(self):
        self.assertEqual(strStr('aaaaa', 'bba'), -1)

    def test_found(self):
        self.assertEqual(strStr('hello', 'll'), 2)

