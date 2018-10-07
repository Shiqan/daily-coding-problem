#!/usr/bin/env python
""" Problem 68 daily-coding-problem.com """
from typing import List, Tuple


def count_opposing_bishops(bishops: List[Tuple[int, int]], m: int) -> int:
    def _count_diagonals(coord: Tuple[int, int], bishops: List[Tuple[int, int]], m: int) -> int:
        result = 0
        for offset, i in enumerate(range(coord[0]+1, m)):
            offset += 1
            left_diagonal = (i, coord[1]-offset)
            right_diagonal = (i, coord[1]+offset)
            if left_diagonal in bishops:
                result += 1
            if right_diagonal in bishops:
                result += 1
        return result

    result = 0
    bishops.sort()

    for bishop in bishops:
        result += _count_diagonals(bishop, bishops, m)

    return result


if __name__ == "__main__":
    bishops = [
        (0, 0),
        (1, 2),
        (2, 2),
        (4, 0),
    ]
    assert count_opposing_bishops(bishops, 5) == 2
