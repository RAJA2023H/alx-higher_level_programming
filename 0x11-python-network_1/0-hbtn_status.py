#!/usr/bin/python3
import urllib.request
# Open and read the content of a URL
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    response = response.read()
    print("Body response:")
    print(f" - type: {type(response)}")
    print(f" - content: {response}")
    response_utf8 = response.decode('utf-8')
    print(f" - utf8 content: {response_utf8}")
