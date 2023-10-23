#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed =0
    for item in range(x):
        try:
            if isinstance(my_list[item], int):
                print("{:d}".format(my_list[item]), end="")
                printed += 1
        except (ValueError, TypeError):
            pass
    print()
    return printed
