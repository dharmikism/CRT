import unittest
from task import Student_Grade_System

class TestAssignment(unittest.TestCase):

    def test1(self):
        self.assertEqual(Student_Grade_System("abc",50,50,50), "Average grade: 50.0, Status: Pass")

    def test2(self):
        self.assertEqual(Student_Grade_System("xyz",12,34,10), "Average grade: 18.66, Status: fail")

    def test3(self):
        self.assertEqual(Student_Grade_System("preeti",90,80,70), "Average grade: 80.0, Status: Pass")

if __name__ == "__main__":
    unittest.main()
