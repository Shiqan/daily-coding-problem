#!/usr/bin/env python
""" Problem 42 daily-coding-problem.com """
from typing import List


def sums_up(S: List[int], k: int) -> List[int]:
    if k == 0:
        return []

    valid_numbers = [n for n in S if 0 < n <= k]
    for i in sorted(valid_numbers, reverse=True):
        remaining_numbers = [n for n in valid_numbers if n != i]
        result = sums_up(remaining_numbers, k - i)
        if result is not None:
            return [i] + result

    return None

if __name__ == "__main__":
    assert sums_up([12, 1, 61, 5, 9, 2], 4) == None
    assert sums_up([12, 1, 61, 5, 9, 2], 11) == [9, 2]
    assert sums_up([12, 1, 61, 5, 9, 2], 24) == [12, 9, 2, 1]