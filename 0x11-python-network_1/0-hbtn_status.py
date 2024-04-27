#!/usr/bin/python3
"""Python script fetch an url"""
import urllib.request
url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    response = response.read()
    response_utf8 = response.decode('utf-8')
    print("Body response:")
    print(f"\t- type: {type(response)}")
    print(f"\t- content: {response}")
    print(f"\t- utf8 content: {response_utf8}")
