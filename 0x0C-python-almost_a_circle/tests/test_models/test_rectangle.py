""" unit test for class rectangle """
import io
import contextlib
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
        self.assertEqual(Rectangle(2, 3, 4, 5).id, 4)

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

    def test_b0_getters(self):
        """testing getters"""
        r = Rectangle(5, 7, 6, 5, 20)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 6)
        self.assertEqual(r.y, 5)
        self.assertEqual(r.id, 20)

    def test_b1_setters(self):
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

    def test_b2_TypeError_width(self):
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

    def test_b3_TypeError_height(self):
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

    def test_b4_TypeError_x(self):
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

    def test_b5_TypeError_y(self):
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

    def test_b6_ValueError_width(self):
        """width is 0"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

        """width is negative"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-32535, 2)

    def test_b7_ValueError_height(self):
        """height is 0"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)

        """height is negative"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -32535)

    def test_b8_ValueError_x(self):

        """x is 0"""
        self.assertEqual(Rectangle(2, 3, 0, 4).x, 0)

        """x is negative"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(22, 3, -3, 4)

    def test_b9_ValueError_y(self):

        """y is 0"""
        self.assertEqual(Rectangle(2, 3, 4, 0).y, 0)

        """y is negative"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(22, 3, 4, -3)


class Test_task4(unittest.TestCase):
    """unit testing for task4"""

    def test_c0_area_method(self):
        """testing area calculations"""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(5, 3, 0, 0, 30).area(), 15)


class Test_task5(unittest.TestCase):
    """unit testing for task5"""

    def test_a0_display__method(self):
        """display, without 'x' and 'y' """
        r1 = Rectangle(2, 3)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), "##\n##\n##\n")

        """display, with 'x' and 'y' """
        r1 = Rectangle(2, 3, 1, 2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), "\n\n ##\n ##\n ##\n")

        """display, with 'x'>0"""
        r2 = Rectangle(5, 4, 1)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r2.display()
        self.assertEqual(f.getvalue(), " #####\n #####\n #####\n #####\n")

        """display, with 'x'=0"""
        r2 = Rectangle(5, 4, 0)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r2.display()
        self.assertEqual(f.getvalue(), "#####\n#####\n#####\n#####\n")

        """display, with x= 0 and 'y' """
        r2 = Rectangle(5, 4, 0, 2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r2.display()
        self.assertEqual(f.getvalue(), "\n\n#####\n#####\n#####\n#####\n")

class Test_task6(unittest.TestCase):
    """unit testing for task6"""

    def test_a0_str1(self):
        """print __str__ case#1"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            print(r1)
        self.assertEqual(f.getvalue(), "[Rectangle] (12) 2/1 - 4/6\n")

    def test_a0_str2(self):
        """printing __str__ case#2"""
        r1 = Rectangle(5, 5, 1)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            print(r1)
        self.assertEqual(f.getvalue(), "[Rectangle] (14) 1/0 - 5/5\n")

class Test_task7(unittest.TestCase):
    """unit testing for task7"""

    def test_a0_str1(self):
        """print_str_case#1"""
        r1 = Rectangle(2, 3, 2, 2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            print(r1)
        self.assertEqual(f.getvalue(), "[Rectangle] (15) 2/2 - 2/3\n")

class Test_task8(unittest.TestCase):
    """unit testing for task8"""

    def test_a0_str1(self):
        """print_str_case#1"""
        r1 = Rectangle(10, 10, 10, 10)
        f = io.StringIO()
        r1.update(89)
        self.assertEqual(r1.id, 89)
        with contextlib.redirect_stdout(f):
            print(r1)
        self.assertEqual(f.getvalue(), "[Rectangle] (89) 10/10 - 10/10\n")

    def test_a0_str2(self):
        """print_str_case#2"""
        r1 = Rectangle(10, 10, 10, 10)
        f = io.StringIO()
        r1.update(89, 2)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        with contextlib.redirect_stdout(f):
            print(r1)
        self.assertEqual(f.getvalue(), "[Rectangle] (89) 10/10 - 2/10\n")

    def test_a0_str3(self):
        """print_str_case#3"""
        r1 = Rectangle(10, 10, 10, 10)
        f = io.StringIO()
        r1.update(89, 2, 3)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        with contextlib.redirect_stdout(f):
            print(r1)
        self.assertEqual(f.getvalue(), "[Rectangle] (89) 10/10 - 2/3\n")

    def test_a0_str4(self):
        """print_str_case#4"""
        r1 = Rectangle(10, 10, 10, 10)
        f = io.StringIO()
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        with contextlib.redirect_stdout(f):
            print(r1)
        self.assertEqual(f.getvalue(), "[Rectangle] (89) 4/10 - 2/3\n")

    def test_a0_str5(self):
        """print_str_case#5"""
        r1 = Rectangle(10, 10, 10, 10)
        f = io.StringIO()
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        with contextlib.redirect_stdout(f):
            print(r1)
        self.assertEqual(f.getvalue(), "[Rectangle] (89) 4/5 - 2/3\n")

class Test_task9(unittest.TestCase):
    """unit testing for task9"""

    def test_a0_str1(self):
        """print_str_case#1"""
        r1 = Rectangle(10, 10, 10, 10)
        f = io.StringIO()
        r1.update(id=89)
        self.assertEqual(r1.id, 89)
        with contextlib.redirect_stdout(f):
            print(r1)
        self.assertEqual(f.getvalue(), "[Rectangle] (89) 10/10 - 10/10\n")

    def test_a0_str2(self):
        """print_str_case#2"""
        r1 = Rectangle(10, 10, 10, 10)
        f = io.StringIO()
        r1.update(id=89, width=2)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        with contextlib.redirect_stdout(f):
            print(r1)
        self.assertEqual(f.getvalue(), "[Rectangle] (89) 10/10 - 2/10\n")

    def test_a0_str3(self):
        """print_str_case#3"""
        r1 = Rectangle(10, 10, 10, 10)
        f = io.StringIO()
        r1.update(id=89, width=2, height=3)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        with contextlib.redirect_stdout(f):
            print(r1)
        self.assertEqual(f.getvalue(), "[Rectangle] (89) 10/10 - 2/3\n")

    def test_a0_str4(self):
        """print_str_case#4"""
        r1 = Rectangle(10, 10, 10, 10)
        f = io.StringIO()
        r1.update(id=89, width=2, height=3, x=4)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        with contextlib.redirect_stdout(f):
            print(r1)
        self.assertEqual(f.getvalue(), "[Rectangle] (89) 4/10 - 2/3\n")

    def test_a0_str5(self):
        """print_str_case#5"""
        r1 = Rectangle(10, 10, 10, 10)
        f = io.StringIO()
        r1.update(id=89, width=2, height=3, x=4, y=5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        with contextlib.redirect_stdout(f):
            print(r1)
        self.assertEqual(f.getvalue(), "[Rectangle] (89) 4/5 - 2/3\n")

    def test_a0_str6(self):
        """print_str_case#5"""
        r1 = Rectangle(10, 10, 10, 10)
        f = io.StringIO()
        r1.update(y=89, id=2, x=3, height=4, width=5)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 89)
        with contextlib.redirect_stdout(f):
            print(r1)
        self.assertEqual(f.getvalue(), "[Rectangle] (2) 3/89 - 5/4\n")
