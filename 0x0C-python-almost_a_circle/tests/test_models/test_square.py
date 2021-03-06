""" unit test for class square """
import io
import pep8
import contextlib
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class Test_task10(unittest.TestCase):
    """unit testing for task10"""

    def test_pep8_model(self):
        """Tests for pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test(self):
        """Tests for pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_00_documentation(self):
        """Test to see if documentation is created and correct"""
        self.assertTrue(hasattr(Square, "__init__"))
        self.assertTrue(Square.__init__.__doc__)
        self.assertTrue(hasattr(Square, "size"))
        self.assertTrue(Square.size.__doc__)
        self.assertTrue(hasattr(Square, "x"))
        self.assertTrue(Square.x.__doc__)
        self.assertTrue(hasattr(Square, "y"))
        self.assertTrue(Square.y.__doc__)
        self.assertTrue(hasattr(Square, "__str__"))
        self.assertTrue(Square.__str__.__doc__)
        self.assertTrue(hasattr(Square, "update"))
        self.assertTrue(Square.update.__doc__)
        self.assertTrue(hasattr(Square, "to_dictionary"))
        self.assertTrue(Square.to_dictionary.__doc__)

    def test_a0_instantiation(self):
        """Testing instances creation"""
        Base._Base__nb_objects = 0
        self.assertEqual(Square(10, 2).id, 1)
        self.assertEqual(Square(4, 2, 3).id, 2)
        self.assertEqual(Square(2, 3, 4, 5).id, 5)

        self.assertEqual(Square(2, 1, 3, 'Holb').id, 'Holb')
        self.assertEqual(Square(2, 1, 2, 'School').id, 'School')
        self.assertEqual(Square(2, 3, 4).id, 3)

        msg = "takes from 2 to 5 positional arguments but 6 were"
        with self.assertRaisesRegex(TypeError, msg):
            Square(22, 3, 4, 3, 5)

        msg = "missing 1 required positional argument: 'size'"
        with self.assertRaisesRegex(TypeError, msg):
            Square()

    def test_a1_getters(self):
        """testing getters for 'size' attrib"""
        s = Square(2, 7, 6, 5)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 7)
        self.assertEqual(s.y, 6)
        self.assertEqual(s.id, 5)

    def test_a2_setters(self):
        """testing setters"""
        s = Square(3, 7, 9, 1)
        s.size = 11
        self.assertEqual(s.size, 11)
        s.size = 22
        self.assertEqual(s.size, 22)

    def test_a3_printing(self):
        """print __str__ case#1"""
        s1 = Square(4, 6, 2, 1)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            print(s1)
        self.assertEqual(f.getvalue(), "[Square] (1) 6/2 - 4\n")

    def test_a4_printing(self):
        """printing __str__ case#2"""
        s1 = Square(5, 5, 1)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            print(s1)
        self.assertEqual(f.getvalue(), "[Square] (4) 5/1 - 5\n")

    def test_a5_display_method_2(self):
        """This function tests the display function"""
        r1 = Square(3)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), "###\n###\n###\n")

    def test_a6_display_method_2(self):
        """This function tests the display function"""
        r1 = Square(3, 1, 3)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), "\n\n\n ###\n ###\n ###\n")


class Test_task11(unittest.TestCase):
    """unit testing for task11"""
    pass


class Test_task12(unittest.TestCase):
    """ unittesting class Rectangle task 10. And now, 12. Square update """

    def test_b1_args(self):
        """ testing positional arguments """
        r1 = Square(50)
        self.assertEqual(r1.size, 50)
        r1.update(10, 22, 14, 5)
        self.assertEqual(r1.size, 22)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.x, 14)
        self.assertEqual(r1.y, 5)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            print(r1)
        self.assertEqual(f.getvalue(), "[Square] (10) 14/5 - 22\n")

    def test_b2_kwargs(self):
        """ testing positional arguments """
        r1 = Square(50)
        self.assertEqual(r1.size, 50)
        r1.update(y=5, id=10, x=14, size=22)
        self.assertEqual(r1.size, 22)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.x, 14)
        self.assertEqual(r1.y, 5)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            print(r1)
        self.assertEqual(f.getvalue(), "[Square] (10) 14/5 - 22\n")


class Test_task14(unittest.TestCase):
    """ unittesting class Rectangle task 10. And now, 12. Square update """

    def test_c0_to_dictionary(self):
        """ updating with a dictionary """
        new_dict = {'x': 14, 'y': 5, 'id': 10, 'size': 22}
        r1 = Square(50)
        self.assertEqual(r1.size, 50)
        r1.update(**new_dict)
        self.assertEqual(r1.size, 22)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.x, 14)
        self.assertEqual(r1.y, 5)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            print(r1)
        self.assertEqual(f.getvalue(), "[Square] (10) 14/5 - 22\n")

    def test_c2_to_dictionary(self):
        """ printing 'dict' type """
        new_dict = {'x': 14, 'y': 5, 'id': 10, 'size': 22}
        r1 = Square(50)
        r1.update(**new_dict)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            print(type(r1.to_dictionary()))
        self.assertEqual(f.getvalue(), "<class 'dict'>\n")
