#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

try:
    bg.area()
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
