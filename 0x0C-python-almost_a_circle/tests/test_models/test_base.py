""" unit test class base """
import unittest
from models.base import Base

class Test_task0(unittest.TestCase):
    """unit testing for task0."""

    def test_a0_instances_creation(self):
        """no args, obj#1"""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base('Holberton').id, 'Holberton')
        self.assertEqual(Base((2,3,4,5,6)).id, (2,3,4,5,6))
        self.assertEqual(Base().id, 3)
        self.assertEqual(Base().id, 4)

    def test_a1_two_args(self):
        """testing TypeError"""
        with self.assertRaises(TypeError):
            Base(2, 'b')

    def test_a2_class_atrib(self):
        """testing private class attribute"""
        with self.assertRaises(AttributeError):
            print(Base(13).__nb_objects)