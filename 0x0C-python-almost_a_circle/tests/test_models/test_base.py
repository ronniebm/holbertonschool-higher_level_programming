""" unit test for max_integer function """
import unittest


from models.base import Base

class TestClassBase(unittest.TestCase):
    """
        unit testing class
    """
    def test_no_args(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_with_args(self):
        b1 = Base(10)
        self.assertEqual(b1.id, 10)
