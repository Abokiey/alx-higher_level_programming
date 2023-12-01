#!/usr/bin/python3
"""send a url request and display the request id"""

import urllib.request
from sys import argv

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        headers = response.info()
        print(headers.get("X-Request-Id"))
