#!/usr/bin/env python
""" Problem 84 daily-coding-problem.com """
from typing import List
import collections

def n_islands(matrix: List[List[int]]) -> int:
    result = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]:
                result += 1
                BFS(i, j, matrix)
    return result
    
def BFS(i: int, j: int, matrix: List[List[int]]):
    def neighbors(i, j):
        return [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]

    Q = collections.deque()
    Q.append((i, j))
    while Q:
        i, j = Q.popleft()
        if 0<=i<len(matrix) and 0<=j<len(matrix[0]) and matrix[i][j]:
            matrix[i][j] = 0
            Q.extend(neighbors(i,j))


if __name__ == "__main__":
    matrix = [
        [1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
    ]
    assert n_islands(matrix) == 4