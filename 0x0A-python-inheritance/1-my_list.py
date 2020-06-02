#!/usr/bin/python3
"""Creating function print_sorted"""


class MyList(list):
    """
     class MyList.

     Arguments:
     ----------
        list  {class} -- [class 'list']
    """
    def print_sorted(self):
        """
        print_sorted method.
        """
        print(sorted(self))
