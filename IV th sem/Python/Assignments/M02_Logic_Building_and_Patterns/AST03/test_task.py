import unittest
from task import sum_of_digits

class TestAssignment(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(sum_of_digits(123), 6)

    def test_single(self):
        self.assertEqual(sum_of_digits(5), 5)

    def test_with_zero(self):
        self.assertEqual(sum_of_digits(105), 6)

if __name__ == "__main__":
    unittest.main()
