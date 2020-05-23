#!/usr/bin/python3
'''100-matrix_mul.py module'''


def matrix_mul(m_a, m_b):
        """
        this function multiplies 2 matrices:

        Arguments:
        ----------
           m_a {list} -- [first matrix]
           m_b {list} -- [second matrix]

        Raises:
        -------
           TypeError1:  [matrices are not list of lists, must be int/float]
           ValueError: [matrices lists are empty, matrices can't be mult.]

        Returns:
        -------
           result of multiplication of two matrices.

        """

        msg = [
                "m_a must be a list",
                "m_b must be a list",
                "m_a must be a list of lists",
                "m_b must be a list of lists",
                "m_a can't be empty",
                "m_b can't be empty",
                "m_a should contain only integers or floats",
                "m_b should contain only integers or floats",
                "each row of m_a must be of the same size",
                "each row of m_b must be of the same size",
                "m_a and m_b can't be multiplied"
        ]

        # case0: matrices should be 'list' type.
        if not isinstance(m_a, list):
                raise TypeError(msg[0])
        if not isinstance(m_b, list):
                raise TypeError(msg[1])

        # case1: 'm_a' and 'm_b' should be a list of lists.
        for row in m_a:
                if not isinstance(row, list):
                        raise TypeError(msg[2])

        for row in m_b:
                if not isinstance(row, list):
                        raise TypeError(msg[3])

        # case2a: 'm_a' and 'm_b' should not be an empty list.
        if not m_a:
                raise ValueError(msg[4])

        if not m_b:
                raise ValueError(msg[5])

        # case2b: lists inside 'm_a' and 'm_b' should not be empty.
        for row in list(map(lambda row: len(row) == 0, m_a)):
                if row == True:
                        raise ValueError(msg[4])

        for row in list(map(lambda row: len(row) == 0, m_b)):
                if row == True:
                        raise ValueError(msg[5])

        # case3: data in matrices should be int/float type only.
        for row in m_a:
                for data in row:
                        if not isinstance(data, int) and not isinstance(data, float):
                                raise TypeError(msg[6])

        for row in m_b:
                for data in row:
                        if not isinstance(data, int) and not isinstance(data, float):
                                raise TypeError(msg[7])

        # case4: all rows in 'm_a' or in 'm_b' must be same size.
        my_list_ma = list(map(lambda row: len(row), m_a))
        len_rows_ma = len(list(dict.fromkeys(my_list_ma)))

        my_list_mb = list(map(lambda row: len(row), m_b))
        len_rows_mb = len(list(dict.fromkeys(my_list_mb)))

        if len_rows_ma != 1:
                raise TypeError(msg[8])

        if len_rows_mb != 1:
                raise TypeError(msg[9])

        # case5: matrix can't be multiplied
        if (len(m_a[0]) != len(m_b)) :
               raise ValueError(msg[10])

        # matrices multiplication procedure:
        new_matrix = []
        new_row = []
        row_a = 0
        row_b = 0
        pos_a = 0
        pos_b = 0
        sum = 0
        i = 0
        j = 0
        k = 0

        for i in range(len(m_a)):
                for j in range(len(m_b[0])):
                        for k in range(len(m_b)):
                                sum += (m_a[row_a][pos_a] * m_b[row_b][pos_b])
                                pos_a += 1
                                row_b += 1

                        pos_a = 0
                        row_b = 0
                        pos_b += 1
                        if len(new_row) <= len(m_b[0]):
                                new_row.append(sum)
                        sum = 0

                pos_b = 0
                row_a += 1
                new_matrix.append(new_row)
                new_row = []

        return(new_matrix)
