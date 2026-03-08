import unittest
from task import number_triangle

class TestAssignment(unittest.TestCase):

    def test_small(self):
        self.assertEqual(number_triangle(2), "1\n12")

    def test_medium(self):
        self.assertEqual(number_triangle(3), "1\n12\n123")

    def test_large(self):
        self.assertEqual(number_triangle(4), "1\n12\n123\n1234")

if __name__ == "__main__":
    unittest.main()
