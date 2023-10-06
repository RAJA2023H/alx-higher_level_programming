#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    l = len(argv)
    if l == 1:
        print("0 arguments.")
    elif l > 1:
        print("{:d} argument{:s}".format(l-1, "s:" if l > 2 else ":"))
        for i in range(1, l):
            print("{:d}: {:s}".format(i, argv[i]))
