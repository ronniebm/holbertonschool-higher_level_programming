#!/usr/bin/python3
""" Default doctstring. """
import urllib.request

if __name__ == "__main__":
    my_url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(my_url) as response:
        html = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf8')))
