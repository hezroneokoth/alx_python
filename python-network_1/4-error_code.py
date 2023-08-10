#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL then displays the body of the response.
If the HTTP status code is greater than or equal to 400, it prints an error message.
"""

import requests
import sys
""" the import scripts"""

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
