#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if my_list is None:
        return my_list
    if 0 <= idx < len(my_list):
        my_list.pop(idx)
    return my_list
