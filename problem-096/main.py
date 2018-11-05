#!/usr/bin/env python
""" Problem 96 daily-coding-problem.com """
from itertools import product

def permutations(iterable, r=None):
    result = []
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield list(pool[i] for i in indices)

if __name__ == "__main__":
    result = permutations([1,2,3]) 
    assert [i for i in result] == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]