""" unit test for class rectangle """
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_task2(unittest.TestCase):
    """unit testing for task2"""

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

    def test_a5_is_subclass(self):
        """ check subclass """
        r = Rectangle(2, 3, 4, 5)
        self.assertTrue(issubclass(type(r), Base))


class Test_task3(unittest.TestCase):
    """unit testing for task3"""

    def test_b1_getters(self):
        """testing getters"""
        r = Rectangle(5, 7, 6, 5, 20)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 6)
        self.assertEqual(r.y, 5)
        self.assertEqual(r.id, 20)

    def test_b2_setters(self):
        """testing setters"""
        r = Rectangle(3, 7, 9, 1, 2)
        r.width = 11
        self.assertEqual(r.width, 11)
        r.height = 22
        self.assertEqual(r.height, 22)
        r.x = 33
        self.assertEqual(r.x, 33)
        r.y = 44
        self.assertEqual(r.y, 44)
        r.id = 55
        self.assertEqual(r.id, 55)

    def test_b3_width_TypeError(self):
        """width is None"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

        """width = string"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("string", 2)

        """width = complex"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(5 + 3j), 2)

        """width = dict"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 5, "b": 2}, 2)

        """width = tuple"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((2, 3, 5, 7), 3)

        """width = list"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([2, 3, 5, 7], 3)

        """width = set"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 3, 5, 7, 9}, 2)

        """width = bool"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def test_b4_height_TypeError(self):
        """height is None"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, None)

        """height = string"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "string")

        """height = complex"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, complex(5 + 3j))

        """height = dict"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {"a": 5, "b": 2})

        """height = tuple"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, (2, 3, 5, 7))

        """height = list"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, [2, 3, 5, 7])

        """height = set"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {1, 3, 5, 7, 9})

        """height = bool"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, True)

    def test_b5_x_TypeError(self):
        """x is None"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 5, None)

        """x = string"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 5, "string")

        """x = complex"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 5, complex(5 + 3j))

        """x = dict"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 5, {"a": 5, "b": 2})

        """x = tuple"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 5, (2, 3, 5, 7))

        """x = list"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 5, [2, 3, 5, 7])

        """x = set"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 5, {1, 3, 5, 7, 9})

        """x = bool"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 5, True)

    def test_b6_y_TypeError(self):
        """y is None"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 5, 1, None)

        """y = string"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 5, 1, "string")

        """y = complex"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 5, 1, complex(5 + 3j))

        """y = dict"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 5, 1, {"a": 5, "b": 2})

        """y = tuple"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 5, 1, (2, 3, 5, 7))

        """y = list"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 5, 1, [2, 3, 5, 7])

        """y = set"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 5, 1, {1, 3, 5, 7, 9})

        """y = bool"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 5, 1, True)

    def test_b7_width_ValueError(self):
        """width is 0"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

        """width is negative"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-32535, 2)

    def test_b8_height_ValueError(self):
        """height is 0"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)

        """height is negative"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -32535)
