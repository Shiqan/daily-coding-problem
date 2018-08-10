#!/usr/bin/env python
""" Problem 12 daily-coding-problem.com """
from typing import List


def staircase_recursive(steps: int) -> int:
    def _helper(steps, cache={}):
        if steps <= 1:
            return 1
            
        if steps not in cache:
            cache[steps] = _helper(steps - 1, cache) + _helper(steps - 2, cache)
        return  cache[steps]

    return _helper(steps)

def staircase_bottom_up(steps: int) -> int:
    result = {
        0: 1,
        1: 1,
    }

    if steps < 0:
        return 0

    if steps <= 1:
        return 1

    for i in range(2, steps+1):
        result[i] = result[i-1] + result[i-2]
    
    return result[steps]

    
def staircase_X(steps: int, X: List[int]) -> int:
    result = {
        0: 1
    }

    if steps < 0:
        return 0

    if steps <= 1:
        return 1

    for i in range(steps+1):
        result[i] = sum(result[i - x] for x in X if i - x > 0)
        result[i] += 1 if i in X else 0
    
    return result[steps]

if __name__ == "__main__":
    assert staircase_recursive(4) == 5
    assert staircase_bottom_up(4) == 5

    r = staircase_X(4, [1, 3, 5])
    assert r == 3
