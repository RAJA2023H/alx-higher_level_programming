#!/usr/bin/python3
def uppercase(str):
    upstr = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
            upstr += char
        else:
            upstr += char
    print("{}".format(upstr))
