import unittest
from task import Collatz_Sequence

class TestAssignment(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(Collatz_Sequence(5), [5, 16, 8, 4, 2, 1])

    def test_multiple_digits(self):
        self.assertEqual(Collatz_Sequence(25), [25, 76, 38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])

    def test_with_zero(self):
        self.assertEqual(Collatz_Sequence(10),[10, 5, 16, 8, 4, 2, 1])

if __name__ == "__main__":
    unittest.main()
