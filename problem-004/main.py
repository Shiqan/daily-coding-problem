#!/usr/bin/env python
""" Problem 4 daily-coding-problem.com """
from typing import List

def find_missing_number(l: List[int]) -> int:
    if not l:
        return

    maximum = max(l)+1
    for i in range(1, maximum):
        if i not in l:
            return i

    return maximum


if __name__ == '__main__':
    l = [3, 4, -1, 1]
    assert find_missing_number(l) == 2

    l = [1, 2, 0]
    assert find_missing_number(l) == 3

    l = []
    assert find_missing_number(l) == None
