#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    prmtrs = {"email": email}
    prmtrs_utf = urllib.parse.urlencode(prmtrs).encode('utf-8')
    r = urllib.request.Request(url, data=prmtrs_utf, method='POST')
    with urllib.request.urlopen(r) as res:
        print(res.read().decode('utf-8'))
