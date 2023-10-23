#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if x > len(my_list):
        x = len(my_list)
    for item in range(x):
        print(my_list[item], end=" ")
    print()
    return x
