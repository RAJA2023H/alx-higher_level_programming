#!/usr/bin/python3
BaseGeometry = __import__('5-base_geometry').BaseGeometry

bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))
print("---- in Python, every class implicitly inherits from 
        the base class object, so calling dir() with an empty 
        class or with object itself as an argument 
        should yield the same result.------")
print(dir(object))
