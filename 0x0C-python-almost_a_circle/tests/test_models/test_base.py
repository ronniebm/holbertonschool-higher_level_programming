""" unit test class base """
import unittest
from models.base import Base

class TestClassBase(unittest.TestCase):
    """
        unit testing class
    """
    def test_a0(self):
        """no args, obj#1"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_a1(self):
        """no args, obj#2"""
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_a2(self):
        """arg is a string, obj#3"""
        b3 = Base('Holberton')
        self.assertEqual(b3.id, 'Holberton')

    def test_a3(self):
        """arg is a tuple, obj#4"""
        b4 = Base((2,3,4,5,6))
        self.assertEqual(b4.id, (2,3,4,5,6))

    def test_a4(self):
        """two obj in one test case, with no args"""
        b5 = Base()
        b6 = Base()
        self.assertEqual(b5.id, 3)
        self.assertEqual(b6.id, 4)

    def test_a5(self):
        """more than one arg"""
        with self.assertRaises(TypeError):
            Base(2, 'b')
            print(Base)

