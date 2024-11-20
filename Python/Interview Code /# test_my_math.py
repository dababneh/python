# test_my_math.py
import unittest
from my_math import add, subtract

class TestMyMath(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = add(3, 4)
        self.assertEqual(result, 7)  # Check if 3 + 4 equals 7

    def test_add_negative_numbers(self):
        result = add(-1, -1)
        self.assertEqual(result, -2)  # Check if -1 + -1 equals -2

    def test_add_zero(self):
        result = add(0, 5)
        self.assertEqual(result, 5)  # Check if 0 + 5 equals 5

    def test_subtract_negative(self):
        result = subtract(4,3)
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()

