#!/bin/bash
#sends request to the url and receive the no. of bytes
curl -s -o /dev/null -w "%{http_size}" "$1"
