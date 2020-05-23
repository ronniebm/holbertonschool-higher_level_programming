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

        # adding two lines '\n\n' after a separator
        for separator in ['. ', ': ', '? ']:
            text = text.replace(separator, '{}\n\n'.format(separator[0]))

        # removing 'newline' for the last line
        print(text, end='')
