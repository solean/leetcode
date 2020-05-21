from ransom_note_383 import can_construct
import unittest

class TestRansomNote(unittest.TestCase):

    def test_1(self):
        self.assertFalse(can_construct('a', 'b'))

    def test_2(self):
        self.assertFalse(can_construct('aa', 'ab'))

    def test_3(self):
        self.assertTrue(can_construct('aa', 'aab'))

