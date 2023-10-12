#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_n = set(my_list)

    for i in my_list:
        if my_list.count(i) == 1:
            unique_n.add(i)

    return sum(unique_n)
