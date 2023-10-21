#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure the tuples have at least 2 elements
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    # Sum the first two elements from each tuple
    result = (a[0] + b[0], a[1] + b[1])
    return result
