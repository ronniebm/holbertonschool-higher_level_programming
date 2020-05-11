#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if (len(tuple_a) == 0):
        c = 0, 0
    if (len(tuple_b) == 0):
        d = 0, 0
    if (len(tuple_a) == 1):
        c = tuple_a[0], 0
    if (len(tuple_b) == 1):
        d = tuple_b[0], 0
    if (len(tuple_a) >= 2):
        c = tuple_a[0], tuple_a[1]
    if (len(tuple_b) >= 2):
        d = tuple_b[0], tuple_b[1]
    return (c[0] + d[0], c[1] + d[1])
