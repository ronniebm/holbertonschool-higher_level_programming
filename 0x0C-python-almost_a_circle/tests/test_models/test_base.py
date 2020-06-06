""" unit test for max_integer function """
import unittest
from models.base import Base

class TestClassBase(unittest.TestCase):
    """
        unit testing class
    """
    def test_a0(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_a1(self):
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_a2(self):
        b3 = Base('Holberton')
        self.assertEqual(b3.id, 'Holberton')

    def test_a3(self):
        b4 = Base((2,3,4,5,6))
        self.assertEqual(b4.id, (2,3,4,5,6))

    def test_a4(self):
        b5 = Base()
        b6 = Base()
        self.assertEqual(b5.id, 3)
        self.assertEqual(b6.id, 4)

    def test_a5(self):
        with self.assertRaises(TypeError):
            Base(2, 'b')
            print(Base)

