#!/usr/bin/python3
for nb in range(100):
    if (nb // 10) != (nb % 10) and (nb // 10) < (nb % 10):
        print("{}{}".format((nb // 10), (nb % 10)), end="")
        if (nb != 89):
            print(", ", end="")
print("")
