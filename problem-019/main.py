#!/usr/bin/env python
""" Problem 19 daily-coding-problem.com """
from typing import List


def min_cost(matrix: List[List[int]]) -> int:
    best_cost = [0] * len(matrix[0])

    for cost in matrix:
        new_best_cost = [0]*len(cost)
        for i in range(len(cost)):
            other_colors = best_cost[:i] + best_cost[i+1:]
            new_best_cost[i] = cost[i] + min(other_colors)
        best_cost = new_best_cost

    return min(best_cost)

if __name__ == "__main__":
    matrix= [
        [1,2,3],
        [4,100,100],
        [6,2,4]
    ]
    assert min_cost(matrix) == 8

    matrix= [
        [1,2,3,4,5],
        [4,100,100,4,4],
        [6,2,4,6,6]
    ]

    assert min_cost(matrix) == 7