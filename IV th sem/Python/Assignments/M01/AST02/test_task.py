import unittest
from task import even_odd

class TestAssignment(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(even_odd(3), "Weird")

    def test_multiple_digits(self):
        self.assertEqual(even_odd(24), "Not Weird")

    def test_with_zero(self):
        self.assertEqual(even_odd(10), "Weird")

if __name__ == "__main__":
    unittest.main()
