#!/usr/bin/python3
"""  Python script that fetches an url"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    r = requests.get(url)
    data = r.text
    rType = type(data)
    print(f"Body response:\n\t- type: {rType}\n\t\
- content: {data}")
