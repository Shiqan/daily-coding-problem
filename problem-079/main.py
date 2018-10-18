#!/usr/bin/env python
""" Problem 79 daily-coding-problem.com """
from typing import List


def make_increasing(arr: List[int]) -> bool:
    decreasing = 0
    for idx, val in enumerate(arr[:-1]):
        if val > arr[idx+1]:
            decreasing += 1
        
    return decreasing <= 1

if __name__ == "__main__":
    assert make_increasing([10, 5, 7]) == True
    assert make_increasing([10, 5, 1]) == False
