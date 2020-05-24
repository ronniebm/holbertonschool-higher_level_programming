#!/usr/bin/python3
'''101-lazy_matrix_mul.py module'''
import numpy


def lazy_matrix_mul(m_a, m_b):
        """
        this function uses numpy to multiply 2 matrices:

        Arguments:
        ----------
           m_a {list} -- [first matrix]
           m_b {list} -- [second matrix]

        Returns:
        -------
           result of multiplication of two matrices.

        """

        return numpy.matmul(m_a, m_b)
