#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for a in range(list_length):
        try:
            result.append(my_list_1[a] / my_list_2[a])
        except ZeroDivisionError:
            print(f"division by 0")
            result.append(0)
        except TypeError:
            print(f"wrong type")
            result.append(0)
        except IndexError:
            print(f"out of range")
    return result
