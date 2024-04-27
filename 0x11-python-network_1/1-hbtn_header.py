#!/usr/bin/python3
"""sends a request to the URL"""
import urllib.request
import sys
url = sys.argv[1]
try:
    with urllib.request.urlopen(url) as response:
        if 'X-Request-Id' in response.headers:
            print(response.headers['X-Request-Id'])
        else:
            print("X-Request-Id header not found in the response")
except Exception as e:
     print("Error:", e)
