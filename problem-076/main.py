#!/usr/bin/env python
""" Problem 76 daily-coding-problem.com """
from typing import List


def order_lexicographically(arr: List[str]) -> int:
    unsorted = 0

    for i in range(len(arr[0])):
        row = [r[i] for r in arr]
        copy_row = row.copy()
        copy_row.sort()
        if row != copy_row:
            unsorted += 1
    return unsorted

if __name__ == "__main__":
    assert order_lexicographically(["cba", "daf", "ghi"]) == 1
    assert order_lexicographically(["abcdef"]) == 0
    assert order_lexicographically(["zyx", "wvu", "tsr"]) == 3
