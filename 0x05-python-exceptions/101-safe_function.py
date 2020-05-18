#!/usr/bin/python3

"""
safe_function: a function that executes a function safely.

@fct: function
@args: arguments.
return: True if integer, else False and prints stderr msg.
"""


#!/usr/bin/python3
def safe_function(fct, *args):
    import sys

    try:
        return (fct(*args))
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
