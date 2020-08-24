#!/usr/bin/python3
""" Default doctstring. """
import urllib.request
import sys

if __name__ == "__main__":
    my_url = sys.argv[1]
    with urllib.request.urlopen('{}'.format(my_url)) as response:
        html = response.headers

print(html._headers[11][1])
