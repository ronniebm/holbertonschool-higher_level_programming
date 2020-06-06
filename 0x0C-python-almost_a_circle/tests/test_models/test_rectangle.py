""" unit test for class rectangle """
import unittest
from models.rectangle import Rectangle


class TestClassRectangle(unittest.TestCase):
    """
        unit testing class Rectangle
    """
    def test_a0(self):
        """creating obj#1 withoud id"""
        b1 = Rectangle(2, 3, 0, 0)
        self.assertEqual(b1.id, 1)

    def test_a1(self):
        """no args, obj#2"""
        b2 = Rectangle(4, 5, 2, 2)
        self.assertTrue(b2.id, 2)

    def test_a2(self):
        """arg is a string, obj#3"""
        b3 = Rectangle(2, 1, 3, 4, 'Holberton')
        self.assertEqual(b3.id, 'Holberton')

    def test_a3(self):
        """arg is a string, obj#3"""
        b3 = Rectangle(2, 1, 2, 4, 'Holberton')
        self.assertEqual(b3.id, 'Holberton')
