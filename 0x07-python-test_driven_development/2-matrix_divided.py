#!/usr/bin/python3
'''2-matrix_divided.py module'''


def matrix_divided(matrix, div):
        """
        this function divides a matrix by a number.

        Arguments:
        ----------
           matrix {list} -- [matrix data must be int/float type]
           div {int} -- [must be an int/float type, different to '0']

        Raises:
        -------
           TypeError: [matrix != list, div/values != (int or float)]
           ZeroDivisionError: [div == 0]

        Returns:
        -------
           new_matrix {list} -- [a new matrix divided by 'div' number]

        """
        new_row = []
        new_matrix = []
        msg = [
                'matrix must be a matrix (list of lists) of integers/floats',
                'Each row of the matrix must have the same size',
                'division by zero',
                'div must be a number'
        ]

        #case0: matrix should not be empty.
        if not matrix:
                raise TypeError(msg[0])

        #case1: matrix should be a list type.
        if not isinstance(matrix, list):
                raise TypeError(msg[0])

        #case2: 'div' must be int/float type only.
        if not isinstance(div, int) and not isinstance(div, float):
                raise TypeError(msg[3])

        for row in matrix:

                # case3: matrix must be a list of lists:
                if not isinstance(row, list):
                        raise TypeError(msg[0])

                # case4: lengh of all rows must be > 0
                if len(row) == 0:
                        raise TypeError(msg[0])

                # case5: 'matrix' data must be int/float type only.
                for element in row:
                        if type(element) != int and type(element) != float:
                                raise TypeError(msg[0])

                # case6: rows should be same size.
                len_row = len(matrix[0])
                if len(row) != len_row:
                        raise TypeError(msg[1])

                # case7: div can't be 0.
                if div == 0:
                        raise ZeroDivisionError(msg[2])

                # normal behaviour.
                for element in row:
                        new_row.append(round(element / div, 2))
                new_matrix.append(new_row)
                new_row = []

        return(new_matrix)
