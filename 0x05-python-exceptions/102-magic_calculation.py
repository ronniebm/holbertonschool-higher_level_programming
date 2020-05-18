#!/usr/bin/python3

"""
magic_calculation: does exactly the same as the python bytecode example.

@a: first integer value.
@b: second integer value.
return: a result.
"""


def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += (a ** b) / i
        except:
            result = a + b
            break
    return (result)
