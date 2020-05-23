#!/usr/bin/python3
'''4-print_square.py module'''


def text_indentation(text):
        """
        prints a text with 2 new lines after {'.', ':', '?' }

        Arguments:
        ----------
           text {str} -- [text to be indented]

        Raises:
        -------
           TypeError:  [text != str]

        Returns:
        -------
           a text indented.

        """

        msg = 'text must be a string'

        # case0: 'text' is not a string.
        if not isinstance(text, str):
            raise TypeError(msg)

        # adding two lines '\n\n' after a separator.
        for separator in ['.', ':', '?']:
            text = text.replace(separator, '{}\n\n'.format(separator))

        # replacing patterns '\n_'.
        while text.find('\n ') != -1:
            text = text.replace('\n ', '\n')

        # removing leading whitespaces.
        text = text.lstrip()

        # printing text indented.
        print(text, end='')
