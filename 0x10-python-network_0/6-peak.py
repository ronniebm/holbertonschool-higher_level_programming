#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    _list = list_of_integers

    if _list == []:
        return None

    size = len(_list)
    if size == 1:
        return _list[0]
    elif size == 2:
        return max(_list)

    MIDDLE = int(size / 2)
    PEAK = _list[MIDDLE]
    if PEAK > _list[MIDDLE - 1] and PEAK > _list[MIDDLE + 1]:
        return PEAK

    elif PEAK < _list[MIDDLE - 1]:
        return find_peak(_list[:MIDDLE])

    else:
        return find_peak(_list[MIDDLE + 1:])
