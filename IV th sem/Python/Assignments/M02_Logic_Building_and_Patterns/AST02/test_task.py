import unittest
from task import reverse_number

class TestAssignment(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(reverse_number(123), 321)

    def test_two_digits(self):
        self.assertEqual(reverse_number(45), 54)

    def test_zero_end(self):
        self.assertEqual(reverse_number(120), 21)

if __name__ == "__main__":
    unittest.main()
