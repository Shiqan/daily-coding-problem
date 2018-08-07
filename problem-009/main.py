#!/usr/bin/env python
""" Problem 9 daily-coding-problem.com """
from typing import List


def find_largest_sum(l: List[int]) -> int:
    include = 0
    exclude = 0
    
    for i in l:
        new_exclude = exclude if exclude > include else include
        
        include = exclude + i
        exclude = new_exclude
     
    return exclude if exclude > include else include

if __name__ == "__main__":
    assert find_largest_sum([2, 4, 6, 2, 5]) == 13
    assert find_largest_sum([5, 1, 1, 5]) == 10    
    assert find_largest_sum([5, 5, 10, 100, 10, 5]) == 110
