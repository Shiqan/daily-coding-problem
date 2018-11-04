#!/usr/bin/env python
""" Problem 95 daily-coding-problem.com """
from typing import List

def next_permuation(nums: List[int]) -> List[int]:
    for i in range(len(nums)-1, -1, -1): 
        if nums[i] > nums[i-1]: 
            break

    if i == 0:
        nums.sort()
        return nums

    smallest = i 
    for j in range(i+1, len(nums)): 
        if nums[j] > nums[i-1] and nums[j] < nums[smallest]: 
            smallest = j

    nums[smallest], nums[i-1] = nums[i-1], nums[smallest]
    return nums[:i] + sorted(nums[i:])


if __name__ == "__main__":
    assert next_permuation([1,2,3]) == [1,3,2]
    assert next_permuation([1,3,2]) == [2,1,3]
    assert next_permuation([3,2,1]) == [1,2,3]
    