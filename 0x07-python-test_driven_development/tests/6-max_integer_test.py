#!/usr/bin/python3
"""
Unittest for max_integer([])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''
    ckas
    '''
    def test_doc(self):
        self.assertTrue(len(max_integer.__doc__) > 1)

    def test_empty(self):
        self.assertIsNone(max_integer([]), None)
        self.assertIsNone(max_integer([None]), None)
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer([7, 1, 10, 16, None])

    def test_one(self):
        self.assertEqual(max_integer([100]), 100)

    def test_integers(self):
        self.assertEqual(max_integer([1, 0, 9, 3]), 9)
        self.assertEqual(max_integer([25, 26, 25, 25]), 26)

    def test_neg(self):
        self.assertEqual(max_integer([-80, -40, -30, -5]), -5)
        self.assertEqual(max_integer([5, 3, 100, -1]), 100)

    def test_float(self):
        self.assertEqual(max_integer([1.1, 3.3, 4, 7.7]), 7.7)
        self.assertEqual(max_integer([-64.5, -50.22, -20.224, -3.14]), -3.14)

    def test_string(self):
        self.assertEqual(max_integer("123453273121"), "7")
        self.assertEqual(max_integer("1, 2, 5"), "5")

    def test_alpha(self):
        self.assertEqual(max_integer(["xyz"]), "xyz")
        self.assertEqual(max_integer(["efg", "1", "4", "xyz"]), "xyz")

    def test_other_type(self):
        self.assertEqual(max_integer([[5, 6, 7], [5, 6, 7]]), [5, 6, 7])

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_docstring(self):
        self.assertTrue(len(__import__('6-max_integer').__doc__) > 1)


if __name__ == "__main__":
    unittest.main()
