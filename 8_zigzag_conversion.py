import unittest

def zigzag_converter(s: str, numRows: int) -> str:
    if numRows == 1:
        return s

    rows = [''] * numRows
    i = 0
    down = True

    for ch in s:
        rows[i] += ch

        if i == 0:
            down = True
        elif i == numRows - 1:
            down = False

        i += 1 if down else -1

    zigzag = ''.join(rows)
    return zigzag


class TestZigZagConverter(unittest.TestCase):

    def test_1_row(self):
        self.assertEqual(zigzag_converter('AB', 1), 'AB')

    def test_3_rows(self):
        self.assertEqual(zigzag_converter('PAYPALISHIRING', 3), 'PAHNAPLSIIGYIR')

    def test_4_rows(self):
        self.assertEqual(zigzag_converter('PAYPALISHIRING', 4), 'PINALSIGYAHRPI')


if __name__ == '__main__':
    unittest.main()
