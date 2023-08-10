#!/usr/bin/python3
"""
Python script that takes GitHub credentials (username and personal access token)
and uses the GitHub API to display the user's id.
"""

import requests
import sys
""" import script"""

if __name__ == "__main__":
    username = hezroneokoth
    token = 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

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))

    try:
        json_response = response.json()
        print(json_response.get("id"))
    except:
        print("None")
