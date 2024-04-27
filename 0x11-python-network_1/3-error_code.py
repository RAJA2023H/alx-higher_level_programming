#!/usr/bin/python3
""" sends a request to the URL and displays the body of the response"""
import urllib.request
import sys


if __name__ == "__main__":
    try:
        URL = sys.argv[1]
        with urllib.request.urlopen(URL) as res:
            print (res.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
