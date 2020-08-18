#!/bin/bash
# display ALL HTTP methods that SERVER will accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
