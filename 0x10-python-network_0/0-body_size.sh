#!/usr/bin/env bash
# shows body size of a given URL.

# [-s]: silent mode   => don't show any error message.
# [-I]: include       => include http response headers!
#                        server name, cookies, date, etc.

curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
