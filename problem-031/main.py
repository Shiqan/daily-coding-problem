#!/usr/bin/env python
""" Problem 31 daily-coding-problem.com """
from string import ascii_letters 

def distance(old: str, new: str) -> int:
    dist = 0
    for c in old:
        if not new:
            dist -= 1

        elif c != new[0]:
            dist += 1

        new = new[1:]

    return dist + len(new)

if __name__ == "__main__":
    assert distance("abc", "abc") == 0
    assert distance("abc", "def") == 3
    assert distance("", "abc") == 3
    assert distance("abc", "") == -3

    assert distance("kitten", "sitting") == 3
    assert distance("hello", "world") == 4
    assert distance("hello-world", "hello-planet") == 6