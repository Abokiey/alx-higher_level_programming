#!/usr/bin/python3

"""takes in a letter and sends a POST request
   to http://0.0.0.0:5000/search_user with the
   letter as a parameter.
"""

from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    resp = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
    try:
        response = resp.json()
        if response == {}:
            print("No result")
        else:
            print(f'[{response.get("id")}] {response.get("name")}')
    except ValueError:
        print("Not a valid JSON")
