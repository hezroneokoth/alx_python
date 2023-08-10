#!/usr/bin/python3
"""Fetches the url and displays the body response.
The script uses the requests package to send an HTTP GET request to the specified URL.
It then displays the type of the response content and the content itself."""

import requests
"""The import script"""
if __name__ == "__main__":
    url = 'https://alu-intranet.hbtn.io/status'
    response = requests.get(url)
   
    print('Body response:')
    print('\t- type:', type(response.text))
    print('\t- content:', response.text)
