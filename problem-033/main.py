#!/usr/bin/env python
""" Problem 33 daily-coding-problem.com """
from typing import List
import bisect


def running_median(arr: List[int]) -> List[int]:
    medians = [arr[0]]
    sorted_arr = [arr[0]]

    for i in arr[1:]:
        bisect.insort(sorted_arr, i)

        length = len(sorted_arr)
        mid = length / 2
        if length % 2 == 0:
            median = sum(sorted_arr[int(mid-1):int(mid+1)]) / 2.0
        else:
            median = sorted_arr[int(mid-0.5)]
        
        medians.append(median)

    return medians


if __name__ == "__main__":
    assert running_median([2, 1, 5, 7, 2, 0, 5]) == [2, 1.5, 2, 3.5, 2, 2, 2]
    assert running_median([5, 15, 1, 3]) == [5, 10, 5, 4]