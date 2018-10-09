#!/usr/bin/env python
""" Problem 70 daily-coding-problem.com """

def perfect_number(n: int) -> int:
    result = 10

    for c in str(n):
        result -= int(c)
    
    return int(str(n) + str(result))


if __name__ == "__main__":
    assert perfect_number(1) == 19
    assert perfect_number(2) == 28
    assert perfect_number(100) == 1