#!/usr/bin/python3
""" Default doctstring. """
import urllib.request as url
import sys

if __name__ == "__main__":
    with url.urlopen(sys.argv[1]) as header:
        print(header.getheader('X-Request-Id'))
