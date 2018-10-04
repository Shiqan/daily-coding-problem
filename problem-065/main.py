#!/usr/bin/env python
""" Problem 65 daily-coding-problem.com """
from typing import List


def spiral(matrix: List[List[int]]) -> List[int]:
    if not matrix:
        return []

    result = []

    result.extend(matrix[0])

    for row in matrix[1:-1]:
        result.append(row[-1])
        
    result.extend(matrix[-1][::-1])

    subresult = []
    for row in matrix[1:-1]:
        subresult.append(row[0])
    result.extend(subresult[::-1])

    matrix = [row[1:-1] for row in matrix[1:-1]]
    result.extend(spiral(matrix))
    return result


if __name__ == "__main__":
    matrix = [
        [1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
    ]

    result = spiral(matrix)
    assert spiral(matrix) == [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]
