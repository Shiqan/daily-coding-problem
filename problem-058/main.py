#!/usr/bin/env python
""" Problem 58 daily-coding-problem.com """
from typing import List


def find_pivot(arr: List[int], low: int, high: int) -> int:
    if high < low:
        return -1
    if high == low:
        return low

    #low + (high - low)/2;
    mid = int((low + high)/2)

    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return (mid-1)
    if arr[low] >= arr[mid]:
        return find_pivot(arr, low, mid-1)
    return find_pivot(arr, mid + 1, high)


def get_index(arr: List[int], e: int) -> int:
    def _helper(arr, e, index):
        arrlength = len(arr)
        i = int(arrlength / 2)
        halfway = arr[i]

        if halfway == e:
            return index+i
            
        if i == 0:
            return None

        if halfway > e:
            return _helper(arr[:i], e, index)
        else:
            index += i
            return _helper(arr[i:], e, index)

    pivot = find_pivot(arr, 0, len(arr)-1)
    if pivot == -1:
        return _helper(arr, e, 0)

    if arr[pivot] == e:
        return pivot

    if arr[0] <= e:
        return _helper(arr[:pivot], e, 0)

    return _helper(arr[pivot+1:], e, pivot+1)


if __name__ == "__main__":
    assert get_index([13, 18, 25, 2, 8, 10], 8) == 4
    assert get_index([13, 18, 25, 2, 8, 10], 13) == 0
    assert get_index([13, 18, 25, 2, 8, 10], 10) == 5
    assert get_index([13, 18, 25, 2, 8, 10], 11) == None
