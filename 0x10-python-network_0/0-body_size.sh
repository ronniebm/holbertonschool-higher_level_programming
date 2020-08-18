#!/usr/bin/env bash
# shows body size of a given URL.
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
