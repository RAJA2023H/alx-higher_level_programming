#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list is None or not my_list:
        return my_list
    if idx < 0 or idx >= len(my_list):
        return my_list
    x = my_list[idx]
    my_list.remove(x)
    return my_list
