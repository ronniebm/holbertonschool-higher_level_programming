#!/usr/bin/python3
""" Default doctstring. """
import urllib.request

if __name__ == "__main__":
    my_url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(my_url) as response:
        html = response.read()

    print("""Body response:
        - type: {}
        - content: {}
        - utf8 content: {}""".format(type(html), html, html.decode("utf-8")))
