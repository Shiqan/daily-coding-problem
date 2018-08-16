#!/usr/bin/env python
""" Problem 18 daily-coding-problem.com """
from typing import List


def max_values_subarrays(array: List[int], k: int) -> List[int]:
    result = []

    for i in range(len(array) - (k-1)):
        result.append(max(array[i:i+3]))

    return result

def max_values_subarrays_alt(array: List[int], k: int) -> List[int]:
    for i in range(k - 1):
        array = [max(a, b) for a, b in zip(array[:-1], array[1:])]

    return array


if __name__ == "__main__":
    assert max_values_subarrays([10, 5, 2, 7, 8, 7], 3) == [10, 7, 8, 8]
    assert max_values_subarrays_alt([10, 5, 2, 7, 8, 7], 3) == [10, 7, 8, 8]
