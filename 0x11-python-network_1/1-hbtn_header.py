#!/usr/bin/python3
"""sends a request to the URL"""
import urllib.request
import sys
url = sys.argv[1]
try:
    r = urllib.request.Request(url)
    with urllib.request.urlopen(r) as response:
        h = response.headers['X-Request-Id']
        print(h)
except Exception as e:
    print("Error:", e)
