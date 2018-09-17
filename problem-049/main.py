#!/usr/bin/env python
""" Problem 49 daily-coding-problem.com """
from typing import List


def max_continguous_sum(numbers: List[int]) -> int:
    result = 0
    continguous_result = 0

    for i in numbers:
        continguous_result += i
        if continguous_result < 0:
            continguous_result = 0
            
        if result < continguous_result:
            result = continguous_result
        
    return result

if __name__ == "__main__":
    assert max_continguous_sum([-5, -1, -8, -9]) == 0
    assert max_continguous_sum([34, -50, 42, 14, -5, 86]) == 137
    assert max_continguous_sum([10, -100, 200, -100, -100]) == 200
    assert max_continguous_sum([10, -9, 200, -100, -100]) == 201
    assert max_continguous_sum([100, 1, -5, 1, 100]) == 197
