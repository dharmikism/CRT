import unittest
from task import Reverse_String

class TestAssignment(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(Reverse_String("hello"), "olleh")

    def test_multiple_digits(self):
        self.assertEqual(Reverse_String("world"), "dlrow")

    def test_with_zero(self):
        self.assertEqual(Reverse_String("python"), "nohtyp")

if __name__ == "__main__":
    unittest.main()
