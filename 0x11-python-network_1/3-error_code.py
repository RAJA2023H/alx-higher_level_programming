#!/usr/bin/python3
""" sends a request to the URL and displays the body of the response"""
import urllib.request
import sys

if __name__ == "__main__":
    try:
        URL = sys.argv[1]
        with urllib.request.urlopen(URL) as res:
            b = response.read().decode('utf-8')
            print (b)
    except rllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
