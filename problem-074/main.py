#!/usr/bin/env python
""" Problem 74 daily-coding-problem.com """

def multiplication_table_occurrences(n: int, x: int) -> int:
    found = 0

    for i in range(n):
        for j in range(n):
            result = (i+1)*(j+1)
            if result == x:
                found += 1

    return found

if __name__ == "__main__":
    assert multiplication_table_occurrences(6, 12) == 4