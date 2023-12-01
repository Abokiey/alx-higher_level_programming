#!/usr/bin/python3
"""takes 2 arguments in order to solve this challenge.
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        argv[2], argv[1])

    resp = requests.get(url)
    commits = resp.json()
    for commit in commits[0:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
