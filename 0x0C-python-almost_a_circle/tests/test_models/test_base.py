""" unit test class base """
import io
import json
import unittest
import contextlib
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class Test_task1(unittest.TestCase):
    """unit testing for task0."""

    def test_a0_instances_creation(self):
        """no args, obj#1"""
        Base._Base__nb_objects = 0
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base('Holberton').id, 'Holberton')
        self.assertEqual(Base((2, 3, 4, 5, 6)).id, (2, 3, 4, 5, 6))
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

        with self.assertRaises(TypeError):
            Base([1, 3], [3, 5])


class Test_task15(unittest.TestCase):
    """ unit testing class Base task 15 """

    def test_b2_dict_to_json(self):
        """ testing positional arguments """
        new_dict = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_json_string([new_dict])
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            print(type(dictionary))
        self.assertEqual(
            f.getvalue(), "<class 'str'>\n")

    def test_b3_json_to_string(self):
        """This function tests the to_json_string"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(
            len(json_dictionary),
            len('[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'))

    def test_b4_to_json_string_withNonearg(self):
        """This function tests to_json_string func with None argument"""
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, "[]")
        self.assertEqual(type(json_dictionary), str)


class Test_task16(unittest.TestCase):
    """ unit testing class Base task 16 """

    def test_c0_save_to_filewithNonearg(self):
        """This function tests the save_to_file func with None argument"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            str = file.read()
        self.assertEqual(len(str), len('[]'))


class Test_task17(unittest.TestCase):
    """ unit testing class Base task 17 """

    def test_d0_from_json_string(self):
        """This function tests the from_json_string func"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output,
                         [{"height": 4, "width": 10, "id": 89},
                          {"height": 7, "width": 1, "id": 7}])
        self.assertEqual(type(list_output), list)

    def test_d1_from_json(self):
        """This function tests the from_json_string func"""
        list_input = []
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [])
        self.assertEqual(type(list_output), list)

    def test_d2_from_json_stringwithNonearg(self):
        """This function tests the from_json_string func"""
        list_output = Rectangle.from_json_string(None)
        self.assertEqual(list_output, [])
        self.assertEqual(type(list_output), list)


class Test_task18(unittest.TestCase):
    """ unit testing class Base task 18 """

    def test_d3_create_zzz(self):
        """This function tests the create func"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), "[Rectangle] (6) 1/0 - 3/5")
        self.assertEqual(str(r2), "[Rectangle] (7) 1/0 - 3/5")
        self.assertEqual(r1 is r2, False)
        self.assertEqual(r1 == r2, False)


class Test_task19(unittest.TestCase):
    """ unit testing class Base task 19 """

    def test_d4_loadfromfile(self):
        """This function tests the create func"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output[0].id,  r1.id)
        self.assertEqual(list_rectangles_output[0].width,  r1.width)
        self.assertEqual(list_rectangles_output[0].height,  r1.height)
        self.assertEqual(list_rectangles_output[0].x,  r1.x)
        self.assertEqual(list_rectangles_output[0].y,  r1.y)
        self.assertEqual(list_rectangles_output[1].id,  r2.id)
        self.assertEqual(list_rectangles_output[1].width,  r2.width)
        self.assertEqual(list_rectangles_output[1].height,  r2.height)
        self.assertEqual(list_rectangles_output[1].x,  r2.x)
        self.assertEqual(list_rectangles_output[1].y,  r2.y)

    def test_load_from_file_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)
