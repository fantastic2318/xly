#!/usr/bin/python
# -*- coding: UTF-8 -*-

def main(x):
    if x >= 0:
        x = list(str(x))
        if int("".join(reverse1(x))) >= 2 ** 31 - 1:
            return 0
        else:
            return int("".join(x))
        index = 0
        while index < len(reverse1(x)) and reverse1(x)[index] == "0":
            index += 1
        return int(''.join(reverse1(x)[index:]))

    else:
        x = abs(x)
        x = list(str(x))
        if -abs(int("".join(reverse1(x)))) < -2 ** 31 - 1:
            return 0
        else:
            return -int("".join(x))


def reverse1(s):
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s


print(main(120))