#!/bin/bash
# do a CURL to a JSON file.
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
