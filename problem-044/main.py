#!/usr/bin/env python
""" Problem 44 daily-coding-problem.com """
from typing import List

def inversions(A: List[int]) -> int:
    result = 0

    for i in range(len(A)):
        _temp = A[i]
        j = i - 1
        while j >= 0 and _temp < A[j]:
            A[j + 1] = A[j]
            result += 1
            j -= 1
        A[j + 1] = _temp

    return result

if __name__ == "__main__":
    assert inversions([1, 2, 3, 4, 5]) == 0
    assert inversions([2, 4, 1, 3, 5]) == 3
    assert inversions([5, 4, 3, 2, 1]) == 10
    