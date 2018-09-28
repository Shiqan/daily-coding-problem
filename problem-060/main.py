#!/usr/bin/env python
""" Problem 60 daily-coding-problem.com """
from typing import List


def find_partition(arr: List[int]) -> bool:
    def _helper(arr: List[int], target: int) -> bool:
        if not arr:
            return False

        if target == 0:
            return True

        return _helper(arr[1:], target) or _helper(arr[1:], target-arr[0])

    summed = sum(arr)
    if summed % 2 == 0:
        half = summed / 2
        return _helper(arr, half)

    return False


if __name__ == "__main__":
    assert find_partition([15, 5, 20, 10, 35, 15, 10]) == True
    assert find_partition([15, 5, 20, 10, 35]) == False
