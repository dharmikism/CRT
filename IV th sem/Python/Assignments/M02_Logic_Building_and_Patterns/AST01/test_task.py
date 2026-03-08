import unittest
from task import count_digits

class TestAssignment(unittest.TestCase):

    def test_single(self):
        self.assertEqual(count_digits(5), 1)

    def test_multiple(self):
        self.assertEqual(count_digits(12345), 5)

    def test_with_zero(self):
        self.assertEqual(count_digits(100), 3)

if __name__ == "__main__":
    unittest.main()
