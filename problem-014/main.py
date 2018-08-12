#!/usr/bin/env python
""" Problem 14 daily-coding-problem.com """
from typing import Callable


def calculate_pi(i: int) -> float:
    return ((4.0 * (-1)**i) / (2*i + 1))

def monte_carlo(f: Callable[[int], float], n: int, decimals: int) -> float:
    result = 0
    for i in range(n):
        result += f(i)

    return round(result, decimals)

if __name__ == "__main__":
    assert monte_carlo(calculate_pi, 1, 3) == 4.0
    assert monte_carlo(calculate_pi, 100000, 3) == 3.141