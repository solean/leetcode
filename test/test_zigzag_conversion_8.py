from zigzag_conversion_8 import zigzag_converter
import unittest

class TestZigZagConverter(unittest.TestCase):

    def test_1_row(self):
        self.assertEqual(zigzag_converter('AB', 1), 'AB')

    def test_3_rows(self):
        self.assertEqual(zigzag_converter('PAYPALISHIRING', 3), 'PAHNAPLSIIGYIR')

    def test_4_rows(self):
        self.assertEqual(zigzag_converter('PAYPALISHIRING', 4), 'PINALSIGYAHRPI')

