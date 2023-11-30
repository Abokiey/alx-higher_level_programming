#!/bin/bash
#sends request to the url and receive the no. of bytes

curl -s -w "%{size_download}\n" "$1" 
