#!/usr/bin/env python
""" Problem 61 daily-coding-problem.com """


def custom_pow(x: int, y: int) -> int:
    if y == 0:
        return 1

    temp = custom_pow(x, int(y / 2))

    if (y % 2 == 0):
        return temp * temp
    else:
        if y > 0:
            return x * temp * temp
        else:
            return (temp * temp) / x


if __name__ == "__main__":
    assert custom_pow(2, 10) == 1024
