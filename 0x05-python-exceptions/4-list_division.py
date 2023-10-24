#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for a in range(0, list_length):
        try:
            result.append(my_list_1[a] / my_list_2[a])
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
    return result
