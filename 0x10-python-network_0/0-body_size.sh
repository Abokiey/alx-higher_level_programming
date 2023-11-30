#!/bin/bash
#sends request to the url and receive the no. of bytes
curl -s "$1" | wc -c
