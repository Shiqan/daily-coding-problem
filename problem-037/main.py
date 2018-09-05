#!/usr/bin/env python
""" Problem 37 daily-coding-problem.com """
from typing import List, Set


def powerset(s: Set[int]) -> List[Set[int]]:
    if not s:
        return [set()]

    r = []
    for i in s:
        set_i = {i}
        for tail in powerset(s - set_i):
            if tail not in r:
                r.append(tail)
                r.append(tail|set_i)
    return r

if __name__ == "__main__":
    assert sorted(powerset({1,2,3}), key=len) == sorted([set(), {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}])
