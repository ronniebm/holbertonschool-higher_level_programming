#!/usr/bin/python3
""" Default doctstring. """
from requests import urllib3

req = urllib3.request.RequestMethods('http://www.voidspace.org.uk')
with urllib.request.urlopen(req) as response:
   the_page = response.read()