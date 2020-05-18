#!/usr/bin/python3

"""
safe_function: a function that executes a function safely.

@fct: function
@args: arguments.
return: True if integer, else False and prints stderr msg.
"""


#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr

    try:
        return (fct(*args))
    except Exception as error:
        print("Exception: {}\n".format(error), file=stderr)
        return None
