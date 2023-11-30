#!/bin/bash
#sends request to the url and receive the no. of bytes

curl -s -i "%{content_size} \n" "$1"
