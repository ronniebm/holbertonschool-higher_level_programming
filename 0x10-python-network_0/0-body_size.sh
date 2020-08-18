#!/usr/bin/env bash
# shows body size of a given URL.

# [-s]: silent mode   => don't show any error message.
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
