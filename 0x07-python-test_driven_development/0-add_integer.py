#!/usr/bin/python3
'''0-add_integer.py module'''


def add_integer(a, b=98):
        """
        this function adds two (2) numbers.

        Arguments:
        ----------
           a {int} -- [1st value]
           b {int} -- [2nd value] (default: {98})

        Raises:
        -------
           TypeError: [a and b must be int/float type only]

        Returns:
        --------
          a value {int} -- [sum of two numbers]

        """

        msg = [
                'a must be an integer',
                'b must be an integer'
        ]

        # case0: 'a' is not int and is not float.
        if type(a) is not int and type(a) is not float:
                raise TypeError(msg[0])

        # case1: 'b' is not int and is not float.
        elif type(b) is not int and type(b) is not float:
                raise TypeError(msg[1])

        # converting 'float' to 'int' for 'a'.
        if isinstance(a, float):
                a = int(a)

        # converting 'float' to 'int' for 'b'.
        if isinstance(b, float):
                b = int(b)

        # returning sum of 'a' and 'b'
        return (a + b)
