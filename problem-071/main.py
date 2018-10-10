#!/usr/bin/env python
""" Problem 71 daily-coding-problem.com """
import random
from collections import defaultdict

def rand7() -> int:
    return random.randint(0,7)

def rand5() -> int:
    r = rand7()
    return r if r <= 5 else rand5()


if __name__ == "__main__":
    d = defaultdict(int)
    for _ in range(100000):
        d[rand5()] += 1

    print(d)