#!/usr/bin/python3
i = 0
while i < 10:
    k = i + 1
    while k < 10 and k != i:
        if i == 8 and k == 9:
            print("{0}{1}".format(i, k))
        else:
            print("{0}{1}, ".format(i, k), end="")
        k += 1
    i += 1
