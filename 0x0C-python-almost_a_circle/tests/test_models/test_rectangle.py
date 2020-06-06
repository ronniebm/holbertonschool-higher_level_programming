""" unit test for class rectangle """
import unittest
from models.rectangle import Rectangle


class Test_task2(unittest.TestCase):
    """unit testing for task2."""

    def test_a0(self):
        """Testing instances creation"""
        self.assertEqual(Rectangle(10, 2).id, 1)
        self.assertEqual(Rectangle(4, 2, 3).id, 2)
        self.assertEqual(Rectangle(2, 3, 4, 5).id, 3)
        self.assertEqual(Rectangle(2, 3, 4, 5, 11).id, 11)
        self.assertEqual(Rectangle(2, 1, 3, 4, 'Holb').id, 'Holb')
        self.assertEqual(Rectangle(2, 1, 2, 4, 'School').id, 'School')

        # Instantiation with no args.
        with self.assertRaises(TypeError):
            Rectangle()

        # Instantiation missing one arg.
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_a1_private_width(self):
        """private width"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_a2_private_height(self):
        """private height"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_a3_private_x(self):
        """private x"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_a4_private_y(self):
        """private y"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)
    
    def test_a5_setter_and_getters(self):
        """getters for all attributes"""
        r = Rectangle(5, 7, 6, 5, 20)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 6)
        self.assertEqual(r.y, 5)
        self.assertEqual(r.id, 20)
        
        

""" class Test_Rectangle_width(unittest.TestCase):
    '''
    Unittests for Rectangle's width.
    '''
    def test_t0(self):
        b1 = Rectangle(2, 3, 0, 0)
 """
