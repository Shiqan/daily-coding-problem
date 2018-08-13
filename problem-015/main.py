#!/usr/bin/env python
""" Problem 15 daily-coding-problem.com """
import random
from typing import Any

def pick(n: int) -> Any:
    random_element = None

    for i, e in enumerate(n):
        if i == 0:
            random_element = e
        elif random.randint(1, i + 1) == 1:
            random_element = e
    return random_element

if __name__ == "__main__":
    assert pick([1]) == 1