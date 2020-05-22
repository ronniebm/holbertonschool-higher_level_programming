#!/usr/bin/python3
'''4-print_square.py module'''


def print_square(size):
        """
        this function prints a square with the character #.

        Arguments:
        ----------
           size {int} -- [size of the square to be printed]

        Raises:
        -------
           TypeError:  [size != int, size == float and < 0]
           ValueError: [size < 0]

        Returns:
        -------
           a square printed with the character #.

        """

        msg = [
                'size must be an integer',
                'size must be >= 0'
        ]

        # case1: 'last_name' is not a string.
        if isinstance(size, float) and size < 0:
                raise TypeError(msg[0])

        # case0: 'size' is not a 'int' type.
        if not isinstance(size, int):
                raise TypeError(msg[0])

        # case2: 'size' is lower than 0.
        if size < 0:
                raise ValueError(msg[1])

        # normal behavior.
        size = int(size)

        for i in range(size):
                print('#' * size)
