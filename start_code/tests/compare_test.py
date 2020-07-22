import unittest

from src.compare import compare

class TestCompare(unittest.TestCase):

    def test_compare_3_1_returns_3_is_greater_than_1(self):
        self.assertEqual("3 is greater than 1", compare(3, 1))

    def test_compare_1_3_returns_1_is_les_than_3(self):
        self.assertEqual("1 is less than 3", compare(1,3))
    
    def test_compare_3_3_returns_the_two_numbers_are_the_same(self):
        self.assertEqual("The two numbers are the same", compare(3,3))