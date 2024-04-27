#!/usr/bin/python3
"""sends a request to the URL"""
import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    r = urllib.request.Request(url)
    with urllib.request.urlopen(r) as response:
        h = response.headers['X-Request-Id']
        print(h)
