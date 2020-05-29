from unique_paths_62 import unique_paths
import unittest

class TestUniquePaths(unittest.TestCase):

    def test_1(self):
        self.assertEqual(unique_paths(3, 2), 3)

    def test_2(self):
        self.assertEqual(unique_paths(7, 3), 28)

    def test_3(self):
        self.assertEqual(unique_paths(23, 12), 193536720)

    def test_4(self):
        self.assertEqual(unique_paths(1, 1), 1)

