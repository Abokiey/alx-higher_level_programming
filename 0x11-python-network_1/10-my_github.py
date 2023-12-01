"""
   takes your GitHub credentials
   and uses the GitHub API to display your id
"""

from sys import argv
import requests


if __name__ == "__main__":
    user = argv[1]
    pwd = argv[2]

    response = resp = requests.get(
        "https://api.github.com/users/{}".format(user),
        headers={"Authorization": "token {}".format(pwd)},
    )
    print(response.json().get("id"))
