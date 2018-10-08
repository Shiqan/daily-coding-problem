#!/usr/bin/env python
""" Problem 69 daily-coding-problem.com """
from typing import List


def find_largest_product(arr: List[int]) -> int:
    def _prod(arr: List[int]) -> int:
        product = 1
        for i in arr:
            product *= i
        return product

    arr.sort()

    min_two = arr[:2]
    max_three = arr[-3:]

    return max(_prod(min_two+[max_three[-1]]), _prod(max_three))

if __name__ == "__main__":
    assert find_largest_product([-10, -10, 5, 2]) == 500
    assert find_largest_product([10, 3, 5, 6, 20]) == 1200
    assert find_largest_product([1, -4, 3, -6, 7, 0]) == 168