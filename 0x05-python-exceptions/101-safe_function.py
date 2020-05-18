#!/usr/bin/python3

"""
safe_function: a function that executes a function safely.

@fct: function
@args: arguments.
return: True if integer, else False and prints stderr msg.
"""


#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        val = fct(*args)
        return (val)
    except Exception as error:
        from sys import stderr
        print("Exception: {}".format(error), file=stderr)
        return None
