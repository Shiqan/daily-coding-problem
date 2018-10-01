#!/usr/bin/env python
""" Problem 63 daily-coding-problem.com """

def n_ways(n: int, m: int) -> int:
    if (n == 1 or m == 1):
        return 1

    return n_ways(n-1,m) + n_ways(n, m-1)

if __name__ == "__main__":
    assert n_ways(2,2) == 2
    assert n_ways(3,3) == 6
    assert n_ways(5,5) == 70