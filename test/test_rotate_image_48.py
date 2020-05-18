from rotate_image_48 import rotate
import unittest

class TestRotateImage(unittest.TestCase):

    def test_1(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]

        rotate(matrix)
        self.assertEqual(len(matrix), 3)
        self.assertCountEqual(matrix[0], expected[0])
        self.assertCountEqual(matrix[1], expected[1])
        self.assertCountEqual(matrix[2], expected[2])

    def test_2(self):
        matrix = [
            [5, 1,  9, 11],
            [2, 4,  8, 10],
            [13, 3,  6, 7],
            [15, 14, 12, 16]
        ]
        expected = [
            [15, 13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7, 10, 11]
        ]

        rotate(matrix)
        self.assertEqual(len(matrix), 4)
        self.assertCountEqual(matrix[0], expected[0])
        self.assertCountEqual(matrix[1], expected[1])
        self.assertCountEqual(matrix[2], expected[2])
        self.assertCountEqual(matrix[3], expected[3])

