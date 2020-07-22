import unittest

from src.compare import compare

class TestCompare(unittest.TestCase):
    # comparing two numbers test either one greater, one less than, or equal
    def test_compare_3_1_returns_3_is_greater_than_1(self):
        self.assertEqual("3 is greater than 1", compare(3, 1))

    def test_compare_3_1_returns_3_is_less_than_1(self):
        self.assertEqual("1 is less than 3", compare(1, 3))
    
    def test_compare_3_1_returns_3_is_equal_to_3(self):
        self.assertEqual("3 is equal to 3", compare(3, 3))