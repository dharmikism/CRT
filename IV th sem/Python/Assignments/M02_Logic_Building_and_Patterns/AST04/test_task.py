import unittest
from task import right_triangle

class TestAssignment(unittest.TestCase):

    def test_small(self):
        self.assertEqual(right_triangle(2), "*\n**")

    def test_medium(self):
        self.assertEqual(right_triangle(3), "*\n**\n***")

    def test_large(self):
        self.assertEqual(right_triangle(4), "*\n**\n***\n****")

if __name__ == "__main__":
    unittest.main()
