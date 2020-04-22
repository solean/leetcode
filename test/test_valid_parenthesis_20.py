from valid_parenthesis_20 import is_valid
import unittest

class TestValidParenthesis(unittest.TestCase):

    def test_valid_paren(self):
        self.assertEqual(is_valid('()'), True)
    
    def test_valid_multiple_types(self):
        self.assertEqual(is_valid('()[]{}'), True)

    def test_invalid_multiple_types(self):
        self.assertEqual(is_valid('(]'), False)

    def test_invalid_order(self):
        self.assertEqual(is_valid('([)]'), False)
    
    def test_valid_nested(self):
        self.assertEqual(is_valid('{[]}'), True)
    
    def test_unclosed(self):
        self.assertEqual(is_valid('['), False)

