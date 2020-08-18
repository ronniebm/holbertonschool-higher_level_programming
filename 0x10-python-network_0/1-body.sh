#!/usr/bin/env bash
# takes in a URL, send a get request, and show response's body.

# [-s]: silent mode   => don't show any error message.
# [-f]: Fail silently => return error 22, instead a 'document failed' from http server!
# [-L]: Location      => if server report 'moved page' this option will make curl redo
#                        the request on the new place.
curl -sfL "$1"
