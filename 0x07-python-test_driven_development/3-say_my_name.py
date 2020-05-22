#!/usr/bin/python3
'''3-say_my_name.py module'''


def say_my_name(first_name, last_name=""):
        """
        this function prints a name: 'first name' + 'last name'.

        Arguments:
        ----------
           first_name {str} -- [first name]
           last_name  {str} -- [last name]

        Raises:
        -------
           TypeError: [first_name != str, last_name != str]

        Returns:
        -------
           My name is <first name> <last name>.

        """

        msg = [
                'first_name must be a string',
                'last_name must be a string'
        ]

        # case0: 'first_name' is not a string.
        if not isinstance(first_name, str):
                raise TypeError(msg[0])

        # case1: 'last_name' is not a string.
        if not isinstance(last_name, str):
                raise TypeError(msg[1])

        # normal behavior.
        print("My name is {} {}".format(first_name, last_name))
